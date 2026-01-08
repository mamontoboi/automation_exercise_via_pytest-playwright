import requests
from endpoints.product_api import ProductAPI


class SearchProductsAPI(ProductAPI):

    def post_to_search_products_of_type(self, text):
        self.response = requests.post(f"{self.BASE_URL}/searchProduct", data={"search_product": text})
        self.response_json = self.response.json()

    def post_to_search_products_without_search_parameter(self):
        self.response = requests.post(f"{self.BASE_URL}/searchProduct")
        self.response_json = self.response.json()


