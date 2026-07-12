import allure
import pytest
from endpoints.login_api import LoginAPI
from utils.allure_reporting import AllureParentSuite, AllureSuiteName, report_case


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.LOGIN,
    sub_suite="Positive Tests",
    title="Login with valid user details",
)
@pytest.mark.api
def test_login_with_valid_user_details():
    LoginAPI() \
        .post_valid_login_details() \
        .check_http_status(200) \
        .check_status_code_from_response_json(200) \
        .check_message_from_response_json("User exists!")


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.LOGIN,
    sub_suite="Negative Tests",
    title="Login with missing email parameter",
)
@pytest.mark.api
def test_login_with_missing_parameter():
    LoginAPI() \
        .post_login_details_with_missing_email() \
        .check_http_status(200) \
        .check_status_code_from_response_json(400) \
        .check_message_from_response_json("Bad request, email or password parameter is missing in POST request.")


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.LOGIN,
    sub_suite="Negative Tests",
    title="Delete login request",
)
@pytest.mark.api
def test_delete_login():
    LoginAPI() \
        .delete_request() \
        .check_http_status(200) \
        .check_status_code_from_response_json(405) \
        .check_message_from_response_json("This request method is not supported.")


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.LOGIN,
    sub_suite="Negative Tests",
    title="Login with invalid user details",
)
@pytest.mark.api
def test_login_with_invalid_details():
    LoginAPI() \
        .post_invalid_login_details() \
        .check_http_status(200) \
        .check_status_code_from_response_json(404) \
        .check_message_from_response_json("User not found!")
