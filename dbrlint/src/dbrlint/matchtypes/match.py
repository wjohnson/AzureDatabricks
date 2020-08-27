import json
from abc import ABC

class Match(ABC):

    @staticmethod
    def try_literal(value):
        output_value = value
        if isinstance(value, str):
            if value == "true":
                output_value = True
            elif value == "false":
                output_value = False
            elif value.isdigit():
                output_value = int(value)
        
        return output_value
            

    @staticmethod
    def traverse_dict(source_dict, key_list):
        if len(key_list) == 1:
            return source_dict.get(key_list[0])
        else:
            key_to_search = key_list[0]
            if source_dict.get(key_to_search) is None:
                return None
            remaining_keys = key_list[1:]
            results = (
                Match
                .traverse_dict(
                    source_dict = source_dict[key_to_search], 
                    key_list = remaining_keys
                )
            )
        return results


    def __init__(self, path, value):
        super().__init__()
        self.path = [x.strip() for x in path.split('.')]
        if isinstance(value, list):
            self.value = [Match.try_literal(v) for v in value]
        else:
            self.value = Match.try_literal(value)

    def evaluate(self, data):
        raise NotImplementedError