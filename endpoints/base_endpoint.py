class BaseEndpoint:

    def __init__(self):
        self.response = None
        self.response_json = None

    def check_status_code(self, code):
        assert self.response.status_code == code

    def check_message_from_response_json(self, expected_message):
        assert self.response_json["message"] == expected_message

    def check_status_code_from_response_json(self, expected_code):
        assert self.response_json["responseCode"] == expected_code
