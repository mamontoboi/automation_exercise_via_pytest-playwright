import os
from dotenv import load_dotenv
from test_data.user import User

load_dotenv()

name = os.getenv("NAME")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

EXISTING_USER = User(name, email, password)
