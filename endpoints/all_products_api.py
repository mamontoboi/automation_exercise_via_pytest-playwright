import logging
import requests
from endpoints.product_api import ProductAPI

logger = logging.getLogger(__name__)

class AllProductsAPI(ProductAPI):

    def get_all_products_list(self):
        logger.info("Getting a list of all products")
        self.response = requests.get(f"{self.BASE_URL}/productsList")
        self.response_json = self.response.json()
        return self

    def post_to_all_product_list(self):
        logger.info("Sending POST request to the list of all products")
        self.response = requests.post(f"{self.BASE_URL}/productsList")
        self.response_json = self.response.json()
        return self
