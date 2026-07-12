import logging
import pytest
import allure
import requests
from endpoints.product_api import ProductAPI

logger = logging.getLogger(__name__)

@pytest.mark.api
class AllProductsAPI(ProductAPI):

    @allure.step("Get all available products list")
    def get_all_products_list(self):
        logger.info("Getting a list of all products")
        self.response = requests.get(f"{self.BASE_URL}/productsList")
        self.response_json = self.response.json()
        return self

    @allure.step("Make invalid post request to get all products list")
    def post_to_all_product_list(self):
        logger.info("Sending POST request to the list of all products")
        self.response = requests.post(f"{self.BASE_URL}/productsList")
        self.response_json = self.response.json()
        return self
