from .match import Match

class ExactMatch(Match):
    def __init__(self, path, value):
        super().__init__(path, value)

    def __str__(self):
        return "ExactMatch: {} should be {}".format('.'.join(self.path), self.value)
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, ExactMatch):
            return self.value == other.value
        return NotImplemented
    
    def evaluate(self, data):
        successfulMatch = False

        
        value_from_data = self.traverse_dict(data, self.path)

        # If the rule is blank, the field should be omitted (value_from_data is None)
        if self.value == "" and value_from_data is None:
            successfulMatch = True
            return successfulMatch

        if isinstance(self.value, list):
            successfulMatch = sorted(value_from_data) == sorted(self.value)
        else:
            successfulMatch = value_from_data == self.value

        return successfulMatch
