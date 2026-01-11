import pytest

@pytest.mark.ui
def test_that_test_cases_page_contains_tests(home_page):
    test_cases_page = home_page.go_to_test_cases_page()
    test_cases_page.check_that_header_is_test_cases()
    test_cases_page.check_that_test_cases_are_present()
