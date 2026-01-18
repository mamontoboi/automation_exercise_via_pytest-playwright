import logging
import requests
from endpoints.product_api import ProductAPI

logger = logging.getLogger(__name__)

class SearchProductsAPI(ProductAPI):

    def post_to_search_products_of_type(self, text):
        logger.info(f"Sending POST request to search for product of type {text}")
        self.response = requests.post(f"{self.BASE_URL}/searchProduct", data={"search_product": text})
        self.response_json = self.response.json()

    def post_to_search_products_without_search_parameter(self):
        logger.info(f"Sending POST request to search for producs without search parameter")
        self.response = requests.post(f"{self.BASE_URL}/searchProduct")
        self.response_json = self.response.json()


