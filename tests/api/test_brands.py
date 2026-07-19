import pytest
from endpoints.all_brands_api import AllBrandsAPI
from utils.allure_reporting import AllureParentSuite, AllureSuiteName, report_case


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.BRANDS,
    sub_suite="Positive Tests",
    title="Get all brands list",
)
@pytest.mark.api
def test_get_all_brands_list():
    AllBrandsAPI() \
        .get_all_brands_list() \
        .check_http_status(200) \
        .check_list_of_brands_is_not_empty() \
        .check_brands_schema()


@report_case(
    parent_suite=AllureParentSuite.API,
    suite=AllureSuiteName.BRANDS,
    sub_suite="Negative Tests",
    title="Put to the brands endpoint",
)
@pytest.mark.api
def test_put_to_all_brands_list():
    AllBrandsAPI() \
        .put_to_all_brands_list() \
        .check_http_status(200) \
        .check_status_code_from_response_json(405) \
        .check_message_from_response_json("This request method is not supported.")
