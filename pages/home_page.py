import logging
from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.login_or_signup_page import LoginOrSignupPage
from pages.contact_us_page import ContactUsPage
from pages.test_cases_page import TestCasesPage
from pages.products_page import ProductsPage
from mixins.subscription_mixin import SubscriptionMixin
from pages.cart_page import CartPage

logger = logging.getLogger(__name__)

class HomePage(BasePage, SubscriptionMixin):

    UAT_URL = "https://automationexercise.com/"
    COOKIE_BUTTON = {"role": "button", "name": "Consent"}
    SIGNUP_LINK = {"role": "link", "name": " Signup / Login"}
    LOGOUT_LINK = {"role": "link", "name": " Logout"}
    CONTACT_US = {"role": "link", "name": " Contact us"}
    DELETE_ACCOUNT_LINK = {"role": "link", "name": " Delete Account"}
    TEST_CASES_LINK = {"role": "link", "name": " Test Cases"}
    PRODUCTS_LINK = {"role": "link", "name": " Products"}
    CART_BUTTON = {"selector": "li a[href*='cart']"}

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

    def logout(self):
        logger.info("Logging out")
        self.page.get_by_role(**self.LOGOUT_LINK).click()
        return LoginOrSignupPage(self.page)
    
    def go_to_contact_us_page(self):
        logger.info("Navigating to Contact Us")
        self.page.get_by_role(**self.CONTACT_US).click()
        return ContactUsPage(self.page)
    
    def go_to_test_cases_page(self):
        logger.info("Navigating to Test Cases")
        self.page.get_by_role(**self.TEST_CASES_LINK).click()
        return TestCasesPage(self.page)
    
    def go_to_products_page(self):
        logger.info("Navigating to Products page")
        self.page.get_by_role(**self.PRODUCTS_LINK).click()
        return ProductsPage(self.page)
    
    def go_to_cart(self):
        logger.info("Open cart")
        self.page.locator(**self.CART_BUTTON).click()
        return CartPage(self.page)
