import logging
import requests
import random
import pytest
import allure
from endpoints.base_endpoint import BaseEndpoint
from faker import Faker
from enum import Enum
from test_data.user import User

logger = logging.getLogger(__name__)


class Title(Enum):
    Mr = "Mr"
    Ms = "Ms"
    Miss = "Miss"


faker = Faker()


@pytest.mark.api
class CreateUser(BaseEndpoint):

    CREATE_USER_URL = f"{BaseEndpoint.BASE_URL}/createAccount"
    DELETE_USER_URL = f"{BaseEndpoint.BASE_URL}/deleteAccount"

    def __init__(self):
        super().__init__()
        self.created_users: list[User] = []

    @allure.step("Generate data for random user creation")
    def generate_random_user(self) -> User:
        """Generate a random user and store it in memory."""
        user = User(
            name=faker.name(),
            email=faker.email(),
            password=faker.password(),
            title=random.choice([Title.Mr.value, Title.Ms.value, Title.Miss.value]),
            birth_date=faker.date_of_birth(minimum_age=18, maximum_age=80),
            lastname=faker.last_name(),
            company=faker.sentence(ext_word_list=["International", "Management", "Leading", "GmbH"]),
            address=faker.address(),
            zipcode=faker.zipcode(),
            country=faker.country(),
            city=faker.city(),
            state=faker.state(),
            mobile_number=faker.phone_number(),
        )
        self.created_users.append(user)
        return user

    @allure.step("Get the last created user from the memory")
    def get_last_created_user(self) -> User | None:
        """Retrieve the last created user."""
        if self.created_users:
            return self.created_users.pop()
        return None

    @allure.step("Create a random user")
    def post_create_random_user(self, user: User | None = None):
        logger.info("Creating a random user")
        if user is None:
            user = self.generate_random_user()
        elif user not in self.created_users:
            self.created_users.append(user)

        payload = user.to_create_account_payload()
        self.response = requests.post(self.CREATE_USER_URL, data=payload)
        self.response_json = self.response.json()
        return self

    @allure.step("Delete the user")
    def delete_last_created_user(self):
        logger.info("Deleting last created user")
        user = self.get_last_created_user()
        if user is None:
            raise AssertionError("No created user is available for deletion")
        self.response = requests.delete(
            self.DELETE_USER_URL,
            data={
                "email": user.email,
                "password": user.password,
            },
        )
        self.response_json = self.response.json()
        return self
