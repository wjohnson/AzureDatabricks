from dbrlint.dbrlinter import DBRLinter
from dbrlint.matchtypes import *

def test_parsing_rules_exact():
    rules_string = "field1: sometext\nfield2: [1,2]".split('\n')
    lint = DBRLinter(rules_string)

    assert(lint.rules[0] == ExactMatch("field1", "sometext"))
    assert(lint.rules[1] == ExactMatch("field2", [1,2]))

def test_parsing_rules_input_required():
    rules_string = "field2: [\"?\"]\nfield3: ?".split('\n')
    lint = DBRLinter(rules_string)

    assert(lint.rules[0] == InputRequired("field2", []))
    assert(lint.rules[1] == InputRequired("field3", "?"))

def test_parsing_rules_input_required_no_quotes():
    rules_string = "field2: [?]\nfield3: ?".split('\n')
    lint = DBRLinter(rules_string)

    assert(lint.rules[0] == InputRequired("field2", []))
    assert(lint.rules[1] == InputRequired("field3", "?"))

def test_parsing_rules_contains():
    rules_string = "field2: [1,2,\"*\"]".split('\n')
    lint = DBRLinter(rules_string)

    assert(lint.rules[0] == ContainsMatch("field2", [1,2]))

def test_parsing_rules_contains_no_quotes():
    rules_string = "field2: [1,2,*]".split('\n')
    lint = DBRLinter(rules_string)

    assert(lint.rules[0] == ContainsMatch("field2", [1,2]))

def test_parsing_rules_contains_no_quotes_middle():
    rules_string = "field2: [1,*,2]".split('\n')
    lint = DBRLinter(rules_string)

    assert(lint.rules[0] == ContainsMatch("field2", [1,2]))