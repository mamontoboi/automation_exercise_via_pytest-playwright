import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
def test_login_successful(page, existing_user) -> None:
    
    home_page = HomePage(page).open()
    home_page.accept_cookies_if_present()
    login_page = home_page.go_to_login_or_signup()
    home_page = login_page.login(existing_user)
    home_page.assert_logged_in(existing_user["name"])
