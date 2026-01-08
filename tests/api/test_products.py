import pytest
from endpoints.all_products_api import AllProductsAPI
from endpoints.search_product_api import SearchProductsAPI


@pytest.mark.api
def test_get_all_products_list():
    list_of_all_products = AllProductsAPI()
    list_of_all_products.get_all_products_list()
    list_of_all_products.check_http_status(200)
    list_of_all_products.check_list_of_products_is_not_empty()
    list_of_all_products.check_products_schema()

@pytest.mark.api
def test_post_to_all_products_list():
    list_of_all_products = AllProductsAPI()
    list_of_all_products.post_to_all_product_list()
    list_of_all_products.check_http_status(200)
    list_of_all_products.check_status_code_from_response_json(405)
    list_of_all_products.check_message_from_response_json("This request method is not supported.")

@pytest.mark.api
def test_post_to_search_product():
    list_of_all_products_of_type = SearchProductsAPI()
    list_of_all_products_of_type.post_to_search_products_of_type("Top")
    list_of_all_products_of_type.check_http_status(200)
    list_of_all_products_of_type.check_list_of_products_is_not_empty()
    list_of_all_products_of_type.check_products_schema()

@pytest.mark.api
def test_post_to_search_product_without_search_parameter():
    list_of_all_products_of_type = SearchProductsAPI()
    list_of_all_products_of_type.post_to_search_products_without_search_parameter()
    list_of_all_products_of_type.check_http_status(200)
    list_of_all_products_of_type.check_status_code_from_response_json(400)
    list_of_all_products_of_type.check_message_from_response_json(
        "Bad request, search_product parameter is missing in POST request."
        )
