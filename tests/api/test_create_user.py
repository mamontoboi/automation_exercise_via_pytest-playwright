import pytest
from endpoints.create_user_api import CreateUser


@pytest.mark.api
def test_create_user(created_users):
    CreateUser(created_users) \
        .post_create_random_user() \
        .check_http_status(200) \
        .check_status_code_from_response_json(201) \
        .check_message_from_response_json("User created!")

@pytest.mark.api
def test_delete_user(created_users):
    """The test is intentionally dependend on the previous test_create_user."""
    CreateUser(created_users) \
        .delete_last_created_user() \
        .check_http_status(200) \
        .check_status_code_from_response_json(200) \
        .check_message_from_response_json("Account deleted!")