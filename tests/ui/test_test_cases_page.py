import pytest
from utils.allure_reporting import AllureParentSuite, AllureSuiteName, report_case


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.TEST_CASES,
    sub_suite="Positive Tests",
    title="Verify the test cases page contains content",
)
@pytest.mark.ui
def test_that_test_cases_page_contains_tests(home_page):
    test_cases_page = home_page.go_to_test_cases_page()
    test_cases_page.check_header_text("Test Cases")
    test_cases_page.check_that_test_cases_are_present()
