import pytest
import allure
from endpoints.create_user_api import CreateUser
from endpoints.login_api import LoginAPI
from utils.allure_reporting import AllureParentSuite, AllureSuiteName, report_case


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.USER_MANAGEMENT,
    severity=allure.severity_level.CRITICAL,
    title="Create a random user and verify login",
)
@pytest.mark.api
def test_create_user():
    creator = CreateUser()
    created_user = creator.generate_random_user()

    creator.post_create_random_user(created_user) \
        .check_http_status(200) \
        .check_status_code_from_response_json(201) \
        .check_message_from_response_json("User created!")

    LoginAPI(created_user) \
        .post_valid_login_details() \
        .check_http_status(200) \
        .check_status_code_from_response_json(200) \
        .check_message_from_response_json("User exists!")


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.USER_MANAGEMENT,
    title="Delete a user",
)
@pytest.mark.api
def test_delete_user():
    CreateUser() \
        .post_create_random_user() \
        .check_http_status(200) \
        .delete_last_created_user() \
        .check_http_status(200) \
        .check_status_code_from_response_json(200) \
        .check_message_from_response_json("Account deleted!")