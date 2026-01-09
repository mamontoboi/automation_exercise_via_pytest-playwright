import pytest
from endpoints.all_brands_api import AllBrandsAPI


@pytest.mark.api
def test_get_all_brands_list():
    list_of_all_brands = AllBrandsAPI()
    list_of_all_brands.get_all_brands_list()
    list_of_all_brands.check_http_status(200)
    list_of_all_brands.check_list_of_brands_is_not_empty()
    list_of_all_brands.check_brands_schema()

@pytest.mark.api
def test_put_to_all_brands_list():
    list_of_all_brands = AllBrandsAPI()
    list_of_all_brands.put_to_all_brands_list()
    list_of_all_brands.check_http_status(200)
    list_of_all_brands.check_status_code_from_response_json(405)
    list_of_all_brands.check_message_from_response_json("This request method is not supported.")
