import logging
from playwright.sync_api import Page, expect
from pages.cart_page import CartPage
from pytest_check import check
from test_data.users import EXISTING_USER

logger = logging.getLogger(__name__)

class ProductPage:
    
    PRODUCT_INFORMATION_CONTAINER = 'div.product-information'
    QUANTITY_INPUT = "input#quantity"
    ADD_TO_CART_BUTTON = "button[type='button'].cart"
    VIEW_CART_LINK = ".modal-content a[href='/view_cart']"
    USER_NAME_FIELD = {"role": "textbox", "name": "Your Name", "exact": True}
    EMAIL_FIELD = {"role": "textbox", "name": "Email Address", "exact": True}
    REVIEW_CONTAINER_HEADER = {"role": "link", "name": "Write Your Review"}
    REVIEW_INPUT_FIELD = {"role": "textbox", "name": "Add Review Here!"}
    SUBMIT_BUTTON = {"role": "button", "name": "Submit"}

    def __init__(self, page: Page):
        self.page = page

    def check_visibility_of_product_details(self):
        logging.info("Check product detail fields")
        expected_fields= "Category", "Availability", "Condition", "Brand"
        product_information_container = self.page.locator(self.PRODUCT_INFORMATION_CONTAINER)
        logging.info("Checking visibility of product title")
        product_name = product_information_container.get_by_role("heading")
        expect (product_name).to_be_visible()
        for field in expected_fields:
            logging.info(f"Checking visibility of {field} field")
            expect(product_information_container.filter(has_text=field)).to_be_visible()

    def check_visibility_of_review_header(self):
        check.is_true(self.page.get_by_role(**self.REVIEW_CONTAINER_HEADER).is_visible())

    def increase_quantity_by_arrow(self):
        """Click the arrow up button (simulate stepUp)"""
        self.page.evaluate(f'const input = document.querySelector("{self.QUANTITY_INPUT}"); input.stepUp();')

    def add_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BUTTON).click()

    def view_cart(self):
        self.page.locator(self.VIEW_CART_LINK).click()
        return CartPage(self.page)

    def add_review(self):
        self.page.get_by_role(**self.USER_NAME_FIELD).fill(EXISTING_USER["name"])
        self.page.get_by_role(**self.EMAIL_FIELD).fill(EXISTING_USER["email"])
        self.page.get_by_role(**self.REVIEW_INPUT_FIELD).fill("Test review here")
        self.page.get_by_role(**self.SUBMIT_BUTTON).click()

    def assert_success_message(self, text):
        logger.info(f"Checking that the text '{text}' is visible")
        expect(self.page.locator("#review-form")).to_contain_text(text)
