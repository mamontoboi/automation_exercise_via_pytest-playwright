import requests
from endpoints.base_endpoint import BaseEndpoint


class AllBrandsAPI(BaseEndpoint):

    @property
    def brands(self):
        return self.response_json.get("brands", [])

    def get_all_brands_list(self):
        self.response = requests.get(f"{self.BASE_URL}/brandsList")
        self.response_json = self.response.json()

    def put_to_all_brands_list(self):
        self.response = requests.put(f"{self.BASE_URL}/brandsList")
        self.response_json = self.response.json()

    def check_list_of_brands_is_not_empty(self):
        assert "brands" in self.response_json
        assert isinstance(self.brands, list)
        assert len(self.response_json) > 0

    def check_brands_schema(self):
        for brand in self.brands:
            assert "id" in brand
            assert "brand" in brand

