import pytest

@pytest.mark.smoke
def test_login_successful(home_page, existing_user):
    login_page = home_page.go_to_login_or_signup()
    home_page = login_page.login(existing_user)
    home_page.assert_logged_in(existing_user["name"])

@pytest.mark.smoke
def test_register_user(home_page, new_user):
    signup_page = home_page.go_to_login_or_signup()
    signup_page.start_signup(new_user)
    signup_page.fill_account_details(new_user)
    signup_page.create_account()
    home_page = signup_page.continue_after_creation()
    home_page.assert_logged_in(new_user["name"])
    home_page.delete_account()
    home_page.assert_account_is_deleted()

@pytest.mark.smoke
def test_login_with_incorrect_password(home_page, existing_user):
    login_page = home_page.go_to_login_or_signup()
    login_page.login_via_wrong_password(existing_user)
    login_page.assert_authentication_error("Your email or password is !")

@pytest.mark.smoke
def test_register_user_with_existing_email(home_page, existing_user):
    signup_page = home_page.go_to_login_or_signup()
    signup_page.start_signup(existing_user)
    signup_page.assert_authentication_error("Email Address already exist!")

@pytest.mark.smoke
def test_logout(home_page, existing_user):
    login_page = home_page.go_to_login_or_signup()
    home_page = login_page.login(existing_user)
    login_page= home_page.logout()
    login_page.check_that_logged_out()
