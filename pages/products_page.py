import logging
from pages.base_page import BasePage
from pages.product_page import ProductPage
from playwright.sync_api import expect

logger = logging.getLogger(__name__)

class ProductsPage(BasePage):

    SEARCH_PRODUCT_FIELD = {"role": "textbox", "name": "Search Product"}
    SEARCHED_PRODUCT_TITLE = ".product-overlay p"
    SUBMIT_BUTTON = "#submit_search"

    def go_to_first_product_details(self):
        logging.info("Navigating to first product details page")
        self.page.get_by_role("link", name=" View Product").first.click()
        return ProductPage(self.page)
    
    def search_product(self, product_name):
        logging.info(f"Searchig for product {product_name}")
        self.page.get_by_role(**self.SEARCH_PRODUCT_FIELD).fill(product_name)
        self.page.locator(self.SUBMIT_BUTTON).click()

    def check_that_searched_product_is_visible(self, product_name):
        logging.info(f"Checking the product {product_name} is visible")
        expect(self.page.locator(self.SEARCHED_PRODUCT_TITLE)).to_contain_text(product_name)

