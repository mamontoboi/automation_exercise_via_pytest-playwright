import logging
import allure
from endpoints.base_endpoint import BaseEndpoint
from test_data.schemas import PRODUCT_LIST_SCHEMA

logger = logging.getLogger(__name__)


class ProductAPI(BaseEndpoint):

    @property
    def products(self):
        return self.response_json.get("products", [])

    @allure.step("Verify the products payload is populated")
    def check_list_of_products_is_not_empty(self):
        logger.info("Checking the list of products is not empty")
        assert "products" in self.response_json
        assert isinstance(self.products, list)
        assert len(self.products) > 0
        return self

    @allure.step("Validate the product list response schema")
    def check_products_schema(self):
        logger.info("Checking the product list response schema")
        return self.check_response_schema(PRODUCT_LIST_SCHEMA)


