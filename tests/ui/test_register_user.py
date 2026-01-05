import pytest
from pages.home_page import HomePage
from pages.signup_page import SignupPage

@pytest.mark.smoke
def test_register_user(page, new_user) -> None:

    home_page = HomePage(page).open()
    home_page.accept_cookies_if_present()
    home_page.go_to_signup()

    signup_page = SignupPage(page)
    signup_page.start_signup(new_user)
    signup_page.fill_account_details(new_user)
    signup_page.create_account()
    signup_page.continue_after_creation()
    signup_page.assert_logged_in(new_user["name"])
    signup_page.delete_account()
    signup_page.assert_account_is_deleted()
