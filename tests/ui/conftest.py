import logging
import pytest
from pathlib import Path
from pytest import FixtureRequest
from playwright.sync_api import Page
# fixtures are discovered by pytest
from fixtures.users import new_user, existing_user  # noqa: F401
from pages.home_page import HomePage

REPORTS_DIR = Path("reports")
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request: FixtureRequest):
    """The fixture processes only rep_call that fails"""
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        test_name = request.node.name
        screenshot_path = SCREENSHOTS_DIR / f"{test_name}.png"
        logging.info(f"Saving the screenshot to {screenshot_path}")
        page.screenshot(
            path=screenshot_path,
            full_page=True,
        )

@pytest.fixture
def home_page(page: Page):
    home = HomePage(page).open()
    home.accept_cookies_if_present()
    yield home
