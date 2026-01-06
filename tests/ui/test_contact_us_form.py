import pytest
from config.paths import TEST_DATA_DIR


@pytest.mark.ui
def test_contact_us_form_success(home_page, existing_user):
    contact_page = home_page.go_to_contact_us_page()
    contact_page.fill_contact_form(existing_user)
    contact_page.attach_file(TEST_DATA_DIR / "simple_import.txt")
    contact_page.submit_message()
    contact_page.assert_success_message("Success! Your details have been submitted successfully.")
