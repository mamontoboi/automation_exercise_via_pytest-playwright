import json
import logging
import pytest
import allure

logger = logging.getLogger(__name__)

@pytest.mark.api
class BaseEndpoint:

    BASE_URL = "https://automationexercise.com/api"

    def __init__(self):
        self.response = None
        self.response_json = None

    def _attach_response_details(self, context_name: str = "response"):
        payload = {
            "url": getattr(self.response, "url", None),
            "status_code": getattr(self.response, "status_code", None),
            "headers": dict(getattr(self.response, "headers", {}) or {}),
        }

        if self.response_json is not None:
            payload["json"] = self.response_json
        else:
            try:
                payload["text"] = self.response.text
            except Exception as exc:  # pragma: no cover - defensive branch
                payload["text_error"] = str(exc)

        allure.attach(
            json.dumps(payload, indent=2, default=str),
            name=f"{context_name}_details.json",
            attachment_type=allure.attachment_type.JSON,
        )

    @allure.step("Verify the response HTTP status")
    def check_http_status(self, expected_code):
        logger.info(f"Checking that the http status code of the response is {expected_code}")
        try:
            assert self.response is not None, "Response is not set"
            actual_status_code = self.response.status_code
            assert actual_status_code == expected_code, f"The actual http status: {actual_status_code}"
        except AssertionError:
            self._attach_response_details("http_status")
            raise
        return self

    @allure.step("Check the message of the response")
    def check_message_from_response_json(self, expected_message):
        logger.info(f"Checking that the message in the response is: {expected_message}")
        try:
            assert self.response_json is not None, "Response is not set"
            actual_message = self.response_json["message"]
            assert actual_message == expected_message, f"The actual message: {actual_message}"
        except AssertionError:
            self._attach_response_details("message")
            raise
        return self

    @allure.step("Check the status code in the message of the response")
    def check_status_code_from_response_json(self, expected_code):
        logger.info(f"Checking that the status code in the response is {expected_code}")
        try:
            assert self.response_json is not None, "Response is not set"
            actual_code = self.response_json["responseCode"]
            assert actual_code == expected_code, f"The actual code: {actual_code}"
        except AssertionError:
            self._attach_response_details("response_code")
            raise
        return self
