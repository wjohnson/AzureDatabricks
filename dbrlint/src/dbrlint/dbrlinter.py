from itertools import compress
import json
import os
import re

from dbrlint.matchtypes import *


from .linter import Linter
class DBRLinter(Linter):
    """
    Accepts rules in the format:
    rule.path.from.json: literal # Exact Matches on a literal
    rule.path.from.json: [lit, lit, ...] # Exact Matches on all of the literal values
    rule.path.from.json: ? # User Input is Required
    rule.path.from.json: ["?"] # User Input is Required and it's an array of values

    """

    @staticmethod
    def _parse_rules(rules):
        rules_ = []
        for rule_set in rules:
            current_rule = None
            try:
                k,v = rule_set.split(':', 1)
            except Exception as e:
                print("Error from rules parsing: {}".format(rule_set))
                raise(e)
            v = v.strip()
            # Fixing this special character for json.loads
            contains_star = re.search(r",?[\s]?(\*),?", v)
            contains_quoted_star = re.search(r"\"\*\"", v)
            # Question mark (?) is indicator for the input required
            if v == "[?]":
                v = '["?"]'
            elif contains_star and not contains_quoted_star:
                start, end = contains_star.span()
                v = v[:(start+1)] + "\"*\"" + v[start+2:]

            if v.startswith("[") and v.endswith("]"):
                # This is an array
                values_array = json.loads(v)
                if "*" in values_array:
                    values_array.pop(values_array.index("*"))
                    current_rule = ContainsMatch(k, values_array)
                elif "?" in values_array:
                    current_rule = InputRequired(k, [])
                else:
                    current_rule = ExactMatch(k, values_array)
            else:
                # This is a literal
                if "?" == v:
                    current_rule = InputRequired(k, "?")
                else:
                    current_rule = ExactMatch(k, v)
            
            if current_rule is None:
                raise TypeError("The following rule failed to be parsed:\n{}".format(rule_set))
            rules_.append(current_rule)
        
        return rules_
            

    def __init__(self, rules_or_path):
        super().__init__()
        if isinstance(rules_or_path, str) and os.path.isfile(rules_or_path):
            with open(rules_or_path, 'r') as fp:
                rules = fp.readlines()
        else:
            rules = rules_or_path
        
        self.rules = DBRLinter._parse_rules(rules)


    def evaluate(self, data):
        errors = []
        failed_evaluation = [not rule.evaluate(data) for rule in self.rules]

        errors = list(compress(
            [str(rule) for rule in self.rules], 
            failed_evaluation
        ))

        return errors
    