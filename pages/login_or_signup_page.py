from playwright.sync_api import Page, expect
import logging

logger = logging.getLogger(__name__)

class LoginOrSignupPage:

    NAME_INPUT = {"role": "textbox", "name": "Name"}
    EMAIL_INPUT = {"text": "Email Address"}
    PASSWORD_INPUT = {"role": "textbox", "name": "Password"}
    LOGIN_BUTTON = {"role": "button", "name": "Login"}
    SIGNUP_BUTTON = {"role": "button", "name": "Signup"}
    TITLE_MR_RADIO = {"role": "radio", "name": "Mr."}
    SIGNUP_PASSWORD_INPUT = {"role": "textbox", "name": "Password *"}
    NEWSLETTER_CHECKBOX = {"role": "checkbox", "name": "Sign up for our newsletter!"}
    SPECIAL_OFFERS_CHECKBOX = {"role": "checkbox", "name": "Receive special offers from"}
    FIRST_NAME_INPUT = {"role": "textbox", "name": "First name *"}
    LAST_NAME_INPUT = {"role": "textbox", "name": "Last name *"}
    ADDRESS_INPUT = {"role": "textbox", "name": "Address * (Street address, P."}
    COUNTRY_SELECT = {"text": "Country *"}
    STATE_INPUT = {"role": "textbox", "name": "State *"}
    CITY_INPUT = {"role": "textbox", "name": "City * Zipcode *"}
    ZIPCODE_INPUT = {"selector": "#zipcode"}
    MOBILE_INPUT = {"role": "textbox", "name": "Mobile Number *"}
    CREATE_ACCOUNT_BUTTON = {"role": "button", "name": "Create Account"}
    CONTINUE_LINK = {"role": "link", "name": "Continue"}


    def __init__(self, page: Page):
        self.page = page

    def login(self, user: dict):
        logger.info("Starting login")
        login_form = self.page.locator("form").filter(has_text="Login")
        login_form.get_by_placeholder(**self.EMAIL_INPUT).fill(user["email"])
        login_form.get_by_role(**self.PASSWORD_INPUT).fill(user["password"])
        self.page.get_by_role(**self.LOGIN_BUTTON).click()

        from pages.home_page import HomePage
        return HomePage(self.page)
        
    def start_signup(self, user: dict):
        logger.info("Starting signup")
        self.page.get_by_role(**self.NAME_INPUT).fill(user["name"])
        self.page.locator("form").filter(has_text="Signup") \
            .get_by_placeholder(**self.EMAIL_INPUT).fill(user["email"])
        self.page.get_by_role(**self.SIGNUP_BUTTON).click()

    def fill_account_details(self, user: dict):
        logger.info("Filling account details")
        self.page.get_by_role(**self.TITLE_MR_RADIO).check()
        self.page.get_by_role(**self.SIGNUP_PASSWORD_INPUT).fill(user["password"])
        self.page.get_by_role(**self.NEWSLETTER_CHECKBOX).check()
        self.page.get_by_role(**self.SPECIAL_OFFERS_CHECKBOX).check()
        self.page.locator("#days").select_option(user["date_of_birth"][0])
        self.page.locator("#months").select_option(user["date_of_birth"][1])
        self.page.locator("#years").select_option(user["date_of_birth"][2])
        self.page.get_by_role(**self.FIRST_NAME_INPUT).fill(user["first_name"])
        self.page.get_by_role(**self.LAST_NAME_INPUT).fill(user["last_name"])
        self.page.get_by_role(**self.ADDRESS_INPUT).fill(user["address"])
        self.page.get_by_label(**self.COUNTRY_SELECT).select_option(user["country"])
        self.page.get_by_role(**self.STATE_INPUT).fill(user["state"])
        self.page.get_by_role(**self.CITY_INPUT).fill(user["city"])
        self.page.locator(**self.ZIPCODE_INPUT).fill(user["zip"])
        self.page.get_by_role(**self.MOBILE_INPUT).fill(user["mobile"])

    def create_account(self):
        logger.info("Creating account")
        self.page.get_by_role(**self.CREATE_ACCOUNT_BUTTON).click()
        expect(self.page.get_by_text("Account Created!")).to_be_visible()

    def continue_after_creation(self):
        self.page.get_by_role(**self.CONTINUE_LINK).click()

        from pages.home_page import HomePage
        return HomePage(self.page)
