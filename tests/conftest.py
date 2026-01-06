import os
import logging
import pytest
from pytest import Item, FixtureRequest
from playwright.sync_api import Page
# fixtures are discovered by pytest
from fixtures.users import new_user, existing_user  # noqa: F401
from pages.home_page import HomePage

REPORTS_DIR = "reports"
TRACES_DIR = os.path.join(REPORTS_DIR, "traces")
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")

os.makedirs(TRACES_DIR, exist_ok=True)
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call):
    """There are three phases in pytest: setup, call (test body) and teardown. 
    The hook runs for each of them, setting attributes to each object
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request: FixtureRequest):
    """The fixture processes only rep_call that fails"""
    yield

    # Runs after the test. request.node is the same as item in the hook
    if request.node.rep_call.failed:
        test_name = request.node.name
        logging.info(f"Saving the screenshot to {SCREENSHOTS_DIR}/{test_name}.png")
        page.screenshot(
            path=f"{SCREENSHOTS_DIR}/{test_name}.png",
            full_page=True,
        )

@pytest.fixture
def home_page(page: Page):
    home = HomePage(page).open()
    home.accept_cookies_if_present()
    yield home
