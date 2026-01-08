import requests
from endpoints.base_endpoint import BaseEndpoint
from test_data.users import EXISTING_USER


class LoginAPI(BaseEndpoint):

    def post_valid_login_details(self):
        payload = {"email": EXISTING_USER["email"], "password": EXISTING_USER["password"]}
        self.response = requests.post(f"{self.BASE_URL}/verifyLogin", data=payload)
        self.response_json = self.response.json()
