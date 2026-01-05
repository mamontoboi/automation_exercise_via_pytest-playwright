from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)

class HomePage:

    UAT_URL = "https://automationexercise.com/"
    COOKIE_BUTTON = {"role": "button", "name": "Consent"}
    SIGNUP_LINK = {"role": "link", "name": " Signup / Login"}

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

    def go_to_signup(self):
        logger.info("Navigating to Signup/Login")
        self.page.get_by_role(**self.SIGNUP_LINK).click()
