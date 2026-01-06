import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
def test_register_user(page, new_user) -> None:

    home_page = HomePage(page).open()
    home_page.accept_cookies_if_present()
    signup_page = home_page.go_to_login_or_signup()
    signup_page.start_signup(new_user)
    signup_page.fill_account_details(new_user)
    signup_page.create_account()
    home_page = signup_page.continue_after_creation()
    home_page.assert_logged_in(new_user["name"])
    home_page.delete_account()
    home_page.assert_account_is_deleted()
