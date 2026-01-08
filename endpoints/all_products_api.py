import requests
from endpoints.product_api import ProductAPI


class AllProductsAPI(ProductAPI):

    def get_all_products_list(self):
        self.response = requests.get(f"{self.BASE_URL}/productsList")
        self.response_json = self.response.json()

    def post_to_all_product_list(self):
        self.response = requests.post(f"{self.BASE_URL}/productsList")
        self.response_json = self.response.json()
