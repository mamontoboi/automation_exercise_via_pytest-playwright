import requests
from endpoints.base_endpoint import BaseEndpoint


class AllBrandList(BaseEndpoint):

    def get_all_brands_list(self):
        self.response = requests.get("https://automationexercise.com/api/brandsList")
        self.response_json = self.response.json()

    def put_to_all_brands_list(self):
        self.response = requests.put("https://automationexercise.com/api/brandsList")
        self.response_json = self.response.json()

    def check_list_of_brands_is_not_empty(self):
        assert len(self.response_json) > 0
