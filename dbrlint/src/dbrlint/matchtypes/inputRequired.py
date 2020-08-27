from .match import Match
class InputRequired(Match):
    def __init__(self, path, value):
        super().__init__(path, value)
    
    def __str__(self):
        return "InputRequired on: {}".format('.'.join(self.path))
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, InputRequired):
            return self.value == other.value
        return NotImplemented
    
    def evaluate(self, data):
        successfulMatch = False

        try:
            value_from_data = self.traverse_dict(data, self.path)
        except KeyError:
            return successfulMatch

        if isinstance(self.value, list):
            # Assuming if User Input is required, the list must be populated
            successfulMatch = len(value_from_data) > 0
        else:
            successfulMatch = value_from_data is not None

        return successfulMatch
