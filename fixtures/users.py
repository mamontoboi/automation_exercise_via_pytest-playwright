from dataclasses import replace
from datetime import date
import pytest
import uuid
from test_data.user import User
from test_data.users import EXISTING_USER


@pytest.fixture
def new_user() -> User:
    return User(
        name="John Doe",
        email=f"john_{uuid.uuid4().hex}@test.com",
        password="123456JohnDoe",
        first_name="John",
        last_name="Doe",
        birth_date=date(2008, 2, 1),
        address="Magic Street 10",
        country="United States",
        state="NY",
        city="NY",
        zipcode="1010",
        mobile_number="123456789",
    )


@pytest.fixture
def existing_user() -> User:
    return replace(EXISTING_USER)
