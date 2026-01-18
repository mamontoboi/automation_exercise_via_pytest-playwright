import requests
from endpoints.base_endpoint import BaseEndpoint
from test_data.users import EXISTING_USER


class LoginAPI(BaseEndpoint):

    def __post_payload_to_login_endpoint(self, payload):
        self.response = requests.post(f"{self.BASE_URL}/verifyLogin", data=payload)
        self.response_json = self.response.json()

    def post_valid_login_details(self):
        payload = {"email": EXISTING_USER["email"], "password": EXISTING_USER["password"]}
        self.__post_payload_to_login_endpoint(payload)

    def post_invalid_login_details(self):
        payload = {"password": EXISTING_USER["password"]}
        self.__post_payload_to_login_endpoint(payload)
