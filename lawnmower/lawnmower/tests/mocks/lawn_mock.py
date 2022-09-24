class LawnMock:
    def __init__(self, expected_is_within_response=False):
        self.expected_is_within_response = expected_is_within_response

    def is_within(self, x, y):
        return self.expected_is_within_response
