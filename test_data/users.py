import os
from dotenv import load_dotenv
from test_data.user import User

load_dotenv()

REQUIRED_ENV_VARS = ("NAME", "EMAIL", "PASSWORD")
missing_env_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
if missing_env_vars:
    raise RuntimeError(
        f"Missing required environment variable(s) for the existing_user fixture: "
        f"{', '.join(missing_env_vars)}. Set them in .env or the environment."
    )

EXISTING_USER = User(
    name=os.getenv("NAME"),
    email=os.getenv("EMAIL"),
    password=os.getenv("PASSWORD"),
)
