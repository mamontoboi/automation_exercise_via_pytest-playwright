import pytest

@pytest.mark.ui
def test_subscription(home_page):
    home_page.subscribe()
    home_page.check_that_subscribed_successfully()
