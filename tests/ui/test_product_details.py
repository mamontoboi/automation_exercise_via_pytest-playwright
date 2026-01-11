import pytest

@pytest.mark.ui
def test_product_details(home_page):
    all_products_page = home_page.go_to_products_page()
    all_products_page.check_header_text("All Products")
    product_details_page = all_products_page.go_to_first_product_details()
    product_details_page.check_visibility_of_product_details()
