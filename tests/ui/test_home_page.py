import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from utils.allure_reporting import AllureParentSuite, AllureSuiteName, report_case


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.BRANDS,
    sub_suite="Negative Tests",
    title="Home page handles an empty brands list without breaking",
)
@pytest.mark.ui
def test_home_page_with_empty_brands_list(page: Page):
    home_page = HomePage(page)
    home_page.mock_empty_brands_list()
    home_page.open()
    home_page.accept_cookies_if_present()
    home_page.assert_brands_list_is_empty()
