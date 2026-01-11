import logging
from pages.base_page import BasePage
from pages.product_page import ProductPage

logger = logging.getLogger(__name__)

class ProductsPage(BasePage):

    def go_to_first_product_details(self):
        logging.info("Navigating to first product details page")
        self.page.get_by_role("link", name=" View Product").first.click()
        return ProductPage(self.page)
