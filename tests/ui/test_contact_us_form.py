import pytest
from config.paths import TEST_DATA_DIR
from utils.allure_reporting import AllureParentSuite, AllureSuiteName, report_case


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.CONTACT_US,
    sub_suite="Positive Tests",
    title="Submit contact form successfully",
)
@pytest.mark.ui
def test_contact_us_form_success(home_page, existing_user):
    contact_page = home_page.go_to_contact_us_page()
    contact_page.fill_contact_form(existing_user)
    contact_page.attach_file(TEST_DATA_DIR / "simple_import.txt")
    contact_page.submit_message()
    contact_page.assert_success_message("Success! Your details have been submitted successfully.")
