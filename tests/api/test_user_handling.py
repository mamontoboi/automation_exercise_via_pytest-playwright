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
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_create_user(user_creator):
    created_user = user_creator.generate_random_user()

    user_creator.post_create_random_user(created_user) \
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
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_delete_user(user_creator):
    user_creator \
        .post_create_random_user() \
        .check_http_status(200) \
        .delete_last_created_user() \
        .check_http_status(200) \
        .check_status_code_from_response_json(200) \
        .check_message_from_response_json("Account deleted!")


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.USER_MANAGEMENT,
    sub_suite="Negative Tests",
    title="Delete a user that does not exist",
)
@pytest.mark.api
def test_delete_nonexistent_user(user_creator):
    user_creator.delete_nonexistent_user() \
        .check_http_status(200) \
        .check_status_code_from_response_json(404) \
        .check_message_from_response_json("Account not found!")


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.USER_MANAGEMENT,
    sub_suite="Negative Tests",
    title="Create a user with a missing required field",
)
@pytest.mark.api
def test_create_user_with_missing_field(user_creator):
    user = user_creator.generate_random_user()
    user_creator.post_create_user_missing_name(user) \
        .check_http_status(200) \
        .check_status_code_from_response_json(400) \
        .check_message_from_response_json("Bad request, name parameter is missing in POST request.")


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.USER_MANAGEMENT,
    sub_suite="Negative Tests",
    title="Create a user with an email that already exists",
)
@pytest.mark.api
def test_create_user_with_duplicate_email(user_creator):
    user = user_creator.generate_random_user()
    user_creator.post_create_random_user(user) \
        .check_http_status(200) \
        .check_status_code_from_response_json(201) \
        .check_message_from_response_json("User created!")

    user_creator.post_create_random_user(user) \
        .check_http_status(200) \
        .check_status_code_from_response_json(400) \
        .check_message_from_response_json("Email already exists!")


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.USER_MANAGEMENT,
    sub_suite="Negative Tests",
    title="Send an unsupported GET request to the create account endpoint",
)
@pytest.mark.api
def test_create_account_unsupported_method():
    CreateUser().get_create_account() \
        .check_http_status(405) \
        .check_detail_from_response_json('Method "GET" not allowed.')


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.USER_MANAGEMENT,
    sub_suite="Negative Tests",
    title="Send an unsupported GET request to the delete account endpoint",
)
@pytest.mark.api
def test_delete_account_unsupported_method():
    CreateUser().get_delete_account() \
        .check_http_status(405) \
        .check_detail_from_response_json('Method "GET" not allowed.')