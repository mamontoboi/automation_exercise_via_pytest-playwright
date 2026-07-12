import pytest
from utils.allure_reporting import AllureParentSuite, AllureSuiteName, report_case


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.SUBSCRIPTION,
    sub_suite="Positive Tests",
    title="Subscribe from the home page",
)
@pytest.mark.ui
def test_subscription_on_home_page(home_page):
    home_page.subscribe()
    home_page.check_that_subscribed_successfully()


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.SUBSCRIPTION,
    sub_suite="Positive Tests",
    title="Subscribe from the cart page",
)
@pytest.mark.ui
def test_subscription_on_cart_page(home_page):
    cart_page = home_page.go_to_cart()
    cart_page.check_card_is_empty()
    cart_page.subscribe()
    cart_page.check_that_subscribed_successfully()
