import logging
import requests
from endpoints.base_endpoint import BaseEndpoint
from test_data.users import EXISTING_USER

logger = logging.getLogger(__name__)

class LoginAPI(BaseEndpoint):

    LOGIN_URL = f"{BaseEndpoint.BASE_URL}/verifyLogin"

    def _post_payload_to_login_endpoint(self, payload: dict):
        self.response = requests.post(self.LOGIN_URL, data=payload)
        self.response_json = self.response.json()
        return self

    def post_valid_login_details(self):
        logger.info("Sending POST request with valid user credentials")
        payload = {"email": EXISTING_USER["email"], "password": EXISTING_USER["password"]}
        return self._post_payload_to_login_endpoint(payload)

    def post_invalid_login_details(self):
        logger.info("Sending POST request with missing email")
        payload = {"password": EXISTING_USER["password"]}
        return self._post_payload_to_login_endpoint(payload)

    def delete_request(self):
        logger.info("Sending DELETE request")
        self.response = requests.delete(self.LOGIN_URL)
        self.response_json = self.response.json()
        return self
