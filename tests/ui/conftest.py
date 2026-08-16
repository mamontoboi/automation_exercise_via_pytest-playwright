import pytest
from playwright.sync_api import Page
# fixtures are discovered by pytest
from fixtures.api_users import user_creator  # noqa: F401
from fixtures.users import existing_user  # noqa: F401
from pages.home_page import HomePage


@pytest.fixture
def home_page(page: Page):
    home = HomePage(page).open()
    home.accept_cookies_if_present()
    yield home
