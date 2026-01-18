import pytest
from endpoints.all_products_api import AllProductsAPI
from endpoints.search_product_api import SearchProductsAPI


@pytest.mark.api
def test_get_all_products_list():
    AllProductsAPI() \
        .get_all_products_list() \
        .check_http_status(200) \
        .check_list_of_products_is_not_empty() \
        .check_products_schema()

@pytest.mark.api
def test_post_to_all_products_list():
    AllProductsAPI() \
        .post_to_all_product_list() \
        .check_http_status(200) \
        .check_status_code_from_response_json(405) \
        .check_message_from_response_json("This request method is not supported.")

@pytest.mark.api
def test_post_to_search_product():
    SearchProductsAPI() \
        .post_to_search_products_of_type("Top") \
        .check_http_status(200) \
        .check_list_of_products_is_not_empty() \
        .check_products_schema()

@pytest.mark.api
def test_post_to_search_product_without_search_parameter():
    SearchProductsAPI() \
        .post_to_search_products_without_search_parameter() \
        .check_http_status(200) \
        .check_status_code_from_response_json(400) \
        .check_message_from_response_json(
        "Bad request, search_product parameter is missing in POST request."
        )
