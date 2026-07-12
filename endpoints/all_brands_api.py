import logging
import allure
import requests
from endpoints.base_endpoint import BaseEndpoint

logger = logging.getLogger(__name__)


class AllBrandsAPI(BaseEndpoint):

    @property
    def brands(self):
        return self.response_json.get("brands", [])

    @allure.step("Retrieve the complete list of brands")
    def get_all_brands_list(self):
        logger.info("Getting a list of all brands")
        self.response = requests.get(f"{self.BASE_URL}/brandsList")
        self.response_json = self.response.json()
        return self

    @allure.step("Send an unsupported PUT request to the brands endpoint")
    def put_to_all_brands_list(self):
        logger.info("Sending PUT request to the list of all brands")
        self.response = requests.put(f"{self.BASE_URL}/brandsList")
        self.response_json = self.response.json()
        return self

    @allure.step("Verify the returned brands payload is populated")
    def check_list_of_brands_is_not_empty(self):
        logger.info("Checking the list of brands is not empty")
        assert "brands" in self.response_json
        assert isinstance(self.brands, list)
        assert len(self.response_json) > 0
        return self

    @allure.step("Validate the brand schema in the response")
    def check_brands_schema(self):
        logger.info("Checking the brand schema")
        for brand in self.brands:
            assert "id" in brand
            assert "brand" in brand
        return self


