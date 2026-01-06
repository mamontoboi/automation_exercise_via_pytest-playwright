from playwright.sync_api import Page, expect
import logging
from pages.login_or_signup_page import LoginOrSignupPage

logger = logging.getLogger(__name__)

class HomePage:

    UAT_URL = "https://automationexercise.com/"
    COOKIE_BUTTON = {"role": "button", "name": "Consent"}
    SIGNUP_LINK = {"role": "link", "name": " Signup / Login"}
    DELETE_ACCOUNT_LINK = {"role": "link", "name": " Delete Account"}

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        logger.info("Opening home page")
        self.page.goto(self.UAT_URL)
        return self

    def accept_cookies_if_present(self):
        btn = self.page.get_by_role(**self.COOKIE_BUTTON)
        if btn.is_visible():
            logger.info("Accepting cookies")
            btn.click()

    def go_to_login_or_signup(self):
        logger.info("Navigating to Signup/Login")
        self.page.get_by_role(**self.SIGNUP_LINK).click()
        return LoginOrSignupPage(self.page)

    def assert_logged_in(self, name: str):
        logger.info(f"Checking that the user {name} is logged in")
        expect(self.page.get_by_text(f"Logged in as {name}")).to_be_visible()

    def delete_account(self):
        logger.info("Deleting account")
        self.page.get_by_role(**self.DELETE_ACCOUNT_LINK).click()

    def assert_account_is_deleted(self):
        logger.info("Checking that account is deleted")
        expect(self.page.get_by_text("Account Deleted!")).to_be_visible()
