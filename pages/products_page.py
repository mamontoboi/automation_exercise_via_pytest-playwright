import allure
import logging
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

logger = logging.getLogger(__name__)

class ProductsPage(BasePage):

    SEARCH_PRODUCT_FIELD = {"role": "textbox", "name": "Search Product"}
    SEARCHED_PRODUCT_TITLE = ".product-overlay p"
    SUBMIT_BUTTON = "#submit_search"
    PRODUCT_CARD = ".features_items .col-sm-4"
    ADD_TO_CART_BUTTON = ".overlay-content a.add-to-cart"
    CONTINUE_SHOPPING = "Continue Shopping"
    VIEW_CART_LINK = {"role": "link", "name": "View Cart"}
    VIEW_PRODUCT_BUTTON = {"role": "link", "name": "View Product"}
    

    @allure.step("Open the details page of the first product")
    def go_to_first_product_details(self):
        logging.info("Navigating to first product details page")
        self.page.get_by_role("link", name=" View Product").first.click()
        return ProductPage(self.page)

    @allure.step("Search for a product by name")
    def search_product(self, product_name):
        logging.info(f"Searchig for product {product_name}")
        self.page.get_by_role(**self.SEARCH_PRODUCT_FIELD).fill(product_name)
        self.page.locator(self.SUBMIT_BUTTON).click()

    @allure.step("Verify the searched product is visible")
    def check_that_searched_product_is_visible(self, product_name):
        logging.info(f"Checking the product {product_name} is visible")
        expect(self.page.locator(self.SEARCHED_PRODUCT_TITLE)).to_contain_text(product_name)

    @allure.step("Add a product by its index from the products list")
    def add_product(self, number):
        product_cart = self.page.locator(self.PRODUCT_CARD).nth(number)
        product_cart.hover()
        add_to_cart_button = product_cart.locator(self.ADD_TO_CART_BUTTON)
        expect(add_to_cart_button).to_be_visible()
        add_to_cart_button.click()

    @allure.step("Add the first product to the cart")
    def add_first_product(self):
        logging.info("Adding the first product on the page")
        self.add_product(0)

    @allure.step("Add the second product to the cart")
    def add_second_product(self):
        logging.info("Adding the second product on the page")
        self.add_product(1)

    @allure.step("Continue shopping after adding a product")
    def continue_shoping(self):
        logging.info("Continue shopping")
        continue_shopping_button = self.page.get_by_text(self.CONTINUE_SHOPPING)
        expect(continue_shopping_button).to_be_visible()
        continue_shopping_button.click()

    @allure.step("Open the cart page from the products page")
    def open_cart(self):
        self.page.get_by_role(**self.VIEW_CART_LINK).click()
        return CartPage(self.page)

    @allure.step("Open the details page of the first visible product")
    def open_first_product_details(self):
        self.page.get_by_role(**self.VIEW_PRODUCT_BUTTON).first.click()
        return ProductPage(self.page)