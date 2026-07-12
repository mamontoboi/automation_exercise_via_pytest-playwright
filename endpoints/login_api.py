import logging
import allure
import requests
from endpoints.base_endpoint import BaseEndpoint
from test_data.user import User
from test_data.users import EXISTING_USER

logger = logging.getLogger(__name__)


class LoginAPI(BaseEndpoint):

    LOGIN_URL = f"{BaseEndpoint.BASE_URL}/verifyLogin"

    def __init__(self, existing_user: User | None = None):
        super().__init__()
        self.user = existing_user or EXISTING_USER

    @allure.step("Send the login request payload to the API")
    def _post_payload_to_login_endpoint(self, payload: dict):
        self.response = requests.post(self.LOGIN_URL, data=payload)
        self.response_json = self.response.json()
        return self

    @allure.step("Submit valid login credentials")
    def post_valid_login_details(self):
        logger.info("Sending POST request with valid user credentials")
        payload = {"email": self.user.email, "password": self.user.password}
        return self._post_payload_to_login_endpoint(payload)

    @allure.step("Submit login credentials without an email address")
    def post_login_details_with_missing_email(self):
        logger.info("Sending POST request with missing email")
        payload = {"password": self.user.password}
        return self._post_payload_to_login_endpoint(payload)

    @allure.step("Send an unsupported DELETE request to the login endpoint")
    def delete_request(self):
        logger.info("Sending DELETE request")
        self.response = requests.delete(self.LOGIN_URL)
        self.response_json = self.response.json()
        return self

    @allure.step("Submit invalid login credentials")
    def post_invalid_login_details(self):
        logger.info("Sending POST request with invalid user details")
        payload = {"email": "not_exist@test.com", "password": "wrong_password"}
        return self._post_payload_to_login_endpoint(payload)
