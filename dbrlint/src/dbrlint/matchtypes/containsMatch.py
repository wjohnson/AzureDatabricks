from .match import Match

class ContainsMatch(Match):
    def __init__(self, path, value):
        super().__init__(path, value)

    def __str__(self):
        return "ContainsMatch: {} should contain {}".format('.'.join(self.path), self.value)
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, ContainsMatch):
            return self.value == other.value
        return NotImplemented
        
    def evaluate(self, data):
        successfulMatch = False

        try:
            value_from_data = self.traverse_dict(data, self.path)
        except KeyError:
            return successfulMatch
        
        successfulMatch = all([(required in value_from_data) for required in self.value])

        return successfulMatch

        