import logging
import allure
import requests
from endpoints.product_api import ProductAPI

logger = logging.getLogger(__name__)


class SearchProductsAPI(ProductAPI):

    @allure.step("Search for products using the supplied keyword")
    def post_to_search_products_of_type(self, text):
        logger.info(f"Sending POST request to search for product of type {text}")
        self.response = requests.post(f"{self.BASE_URL}/searchProduct", data={"search_product": text})
        self.response_json = self.response.json()
        return self

    @allure.step("Submit a search request without a search parameter")
    def post_to_search_products_without_search_parameter(self):
        logger.info("Sending POST request to search for producs without search parameter")
        self.response = requests.post(f"{self.BASE_URL}/searchProduct")
        self.response_json = self.response.json()
        return self



