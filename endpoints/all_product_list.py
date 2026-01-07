import requests
from endpoints.base_endpoint import BaseEndpoint


class AllProductList(BaseEndpoint):

    def get_all_products_list(self):
        self.response = requests.get("https://automationexercise.com/api/productsList")
        self.response_json = self.response.json()

    def post_to_search_products_of_type(self, text):
        self.response = requests.post(
            "https://automationexercise.com/api/searchProduct", 
            data={"search_product": text}
            )
        self.response_json = self.response.json()

    def check_list_of_products_is_not_empty(self):
        assert len(self.response_json) > 0
