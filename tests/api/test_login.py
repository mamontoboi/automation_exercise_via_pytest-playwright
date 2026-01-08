import pytest
from endpoints.login_api import LoginAPI


@pytest.mark.api
def test_to_verify_login_with_valid_details():
    login_request = LoginAPI()
    login_request.post_valid_login_details()
    login_request.check_http_status(200)
    login_request.check_status_code_from_response_json(200)
    login_request.check_message_from_response_json("User exists!")
