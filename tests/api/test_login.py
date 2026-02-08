import pytest
from endpoints.login_api import LoginAPI


@pytest.mark.api
def test_login_with_valid_user_details():
    LoginAPI() \
        .post_valid_login_details() \
        .check_http_status(200) \
        .check_status_code_from_response_json(200) \
        .check_message_from_response_json("User exists!")

@pytest.mark.api
def test_login_with_missing_parameter():
    LoginAPI() \
        .post_login_details_with_missing_email() \
        .check_http_status(200) \
        .check_status_code_from_response_json(400) \
        .check_message_from_response_json("Bad request, email or password parameter is missing in POST request.")

@pytest.mark.api
def test_delete_login():
    LoginAPI() \
        .delete_request() \
        .check_http_status(200) \
        .check_status_code_from_response_json(405) \
        .check_message_from_response_json("This request method is not supported.")
    
@pytest.mark.api
def test_login_with_invalid_details():
    LoginAPI() \
        .post_invalid_login_details() \
        .check_http_status(200) \
        .check_status_code_from_response_json(404) \
        .check_message_from_response_json("User not found!")
