import logging
import requests
import random
from endpoints.base_endpoint import BaseEndpoint
from faker import Faker
from enum import Enum

logger = logging.getLogger(__name__)

class Title(Enum):
    Mr = "Mr"
    Ms = "Ms"
    Miss = "Miss"
    
faker = Faker()

class CreateUser(BaseEndpoint):

    CREATE_USER_URL = f"{BaseEndpoint.BASE_URL}/createAccount"
    DELETE_USER_URL = f"{BaseEndpoint.BASE_URL}/deleteAccount"

    # Store created users in fixture memory
    def __init__(self, created_users):
        self.created_users = created_users

    def generate_random_user(self):
        """Generate a random user and store it in memory."""
        user = {
            "name": faker.name(),
            "email": faker.email(),
            "password": faker.password(),
            "title": random.choice([Title.Mr, Title.Ms, Title.Miss]),
            "birth_date": faker.date_of_birth(minimum_age=18, maximum_age=80),
            "lastname": faker.last_name(),
            "company": faker.sentence(ext_word_list=["International", "Management", "Leading", "GmbH"]),
            "address": faker.address(),
            "zipcode": faker.zipcode(),
            "country": faker.country(),
            "city": faker.city(),
            "state": faker.state(),
            "mobile_number": faker.phone_number()
        }
        self.created_users.append(user)
        return user

    def get_last_created_user(self):
        """Retrieve the last created user."""
        if self.created_users:
            return self.created_users.pop()
        return None

    def post_create_random_user(self):
        logger.info("Creating a random user")
        user = self.generate_random_user()
        payload = {
            "name": user["name"],
            "email": user["email"],
            "password": user["password"],
            "title": user["title"].value,
            "birth_year": user["birth_date"].strftime("%Y"),
            "birth_month": user["birth_date"].strftime("%m"),
            "birth_date": user["birth_date"].strftime("%d"),
            "firstname": user["name"],
            "lastname": user["lastname"],
            "company": user["company"],
            "address1": user["address"],
            "address2": user["address"],
            "country": user["country"],
            "zipcode": user["zipcode"],
            "state": user["state"],
            "city": user["city"],
            "mobile_number": user["mobile_number"]
        }
        self.response = requests.post(self.CREATE_USER_URL, data=payload)
        self.response_json = self.response.json()
        return self

    def delete_last_created_user(self):
        logger.info("Deleting last created user")
        user = self.get_last_created_user()
        self.response = requests.delete(self.DELETE_USER_URL, 
                                        data={
                                            "email": user["email"],
                                            "password": user["password"]
                                            }
                                        )
        self.response_json = self.response.json()
        return self
