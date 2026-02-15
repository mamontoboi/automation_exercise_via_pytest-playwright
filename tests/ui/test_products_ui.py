import pytest

@pytest.mark.ui
def test_product_details(home_page):
    all_products_page = home_page.go_to_products_page()
    all_products_page.check_header_text("All Products")
    product_details_page = all_products_page.go_to_first_product_details()
    product_details_page.check_visibility_of_product_details()

@pytest.mark.ui
def test_search_product(home_page):
    all_products_page = home_page.go_to_products_page()
    all_products_page.check_header_text("All Products")
    all_products_page.search_product("Blue Top")
    all_products_page.check_header_text("Searched Products")
    all_products_page.check_that_searched_product_is_visible("Blue Top")

@pytest.mark.ui
def test_add_products_to_cart(home_page):
    all_products_page = home_page.go_to_products_page()
    all_products_page.check_header_text("All Products")
    all_products_page.add_first_product()
    all_products_page.continue_shoping()
    all_products_page.add_second_product()
    cart_page = all_products_page.open_cart()
    cart_page.check_number_of_items_in_cart(2)
