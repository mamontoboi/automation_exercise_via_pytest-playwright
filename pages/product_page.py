import logging
from playwright.sync_api import Page, expect

logger = logging.getLogger(__name__)

class ProductPage:

    PRODUCT_INFORMATION_CONTAINER = 'div.product-information'
    
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
            expect (product_information_container.filter(has_text=field)).to_be_visible()


