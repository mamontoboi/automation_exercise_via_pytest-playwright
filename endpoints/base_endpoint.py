class BaseEndpoint:

    BASE_URL = "https://automationexercise.com/api"

    def __init__(self):
        self.response = None
        self.response_json = None

    def check_http_status(self, expected):
        assert self.response is not None, "Response is not set"
        assert self.response.status_code == expected

    def check_message_from_response_json(self, expected_message):
        assert self.response_json is not None, "Response is not set"
        assert self.response_json["message"] == expected_message

    def check_status_code_from_response_json(self, expected_code):
        assert self.response_json is not None, "Response is not set"
        assert self.response_json["responseCode"] == expected_code
