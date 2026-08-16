import pytest
from endpoints.create_user_api import CreateUser


@pytest.fixture
def user_creator():
    creator = CreateUser()
    yield creator
    while creator.created_users:
        creator.delete_last_created_user()
