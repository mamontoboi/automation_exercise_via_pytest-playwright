from dataclasses import replace
import pytest
from test_data.user import User
from test_data.users import EXISTING_USER


@pytest.fixture
def existing_user() -> User:
    return replace(EXISTING_USER)
