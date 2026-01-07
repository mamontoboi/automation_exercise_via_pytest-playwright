import pytest
from endpoints.all_product_list import AllProductList

@pytest.mark.api
def test_get_all_products_list():
    list_of_all_products = AllProductList()
    list_of_all_products.get_all_products_list()
    list_of_all_products.check_status_code(200)
    list_of_all_products.check_list_of_products_is_not_empty()

@pytest.mark.api
def test_post_to_search_product():
    list_of_all_products_of_type = AllProductList()
    list_of_all_products_of_type.post_to_search_products_of_type("Top")
    list_of_all_products_of_type.check_status_code(200)
    list_of_all_products_of_type.check_list_of_products_is_not_empty()
