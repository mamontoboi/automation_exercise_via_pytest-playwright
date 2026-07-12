import pytest

from utils.allure_reporting import AllureParentSuite, AllureSuiteName, report_case


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.PRODUCTS,
    sub_suite="Positive Tests",
    title="Open product details",
)
@pytest.mark.ui
def test_product_details(home_page):
    all_products_page = home_page.go_to_products_page()
    all_products_page.check_header_text("All Products")
    product_details_page = all_products_page.go_to_first_product_details()
    product_details_page.check_visibility_of_product_details()


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.PRODUCTS,
    sub_suite="Positive Tests",
    title="Search for a product",
)
@pytest.mark.ui
def test_search_product(home_page):
    all_products_page = home_page.go_to_products_page()
    all_products_page.check_header_text("All Products")
    all_products_page.search_product("Blue Top")
    all_products_page.check_header_text("Searched Products")
    all_products_page.check_that_searched_product_is_visible("Blue Top")


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.PRODUCTS,
    sub_suite="Positive Tests",
    title="Add products to the cart",
)
@pytest.mark.ui
def test_add_products_to_cart(home_page):
    all_products_page = home_page.go_to_products_page()
    all_products_page.check_header_text("All Products")
    all_products_page.add_first_product()
    all_products_page.continue_shoping()
    all_products_page.add_second_product()
    cart_page = all_products_page.open_cart()
    cart_page.check_number_of_items_in_cart(2)


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.PRODUCTS,
    sub_suite="Positive Tests",
    title="Increase product quantity from details page",
)
@pytest.mark.ui
def test_add_4_products_to_cart(home_page):
    all_products_page = home_page.go_to_products_page()
    product_details_page = all_products_page.go_to_first_product_details()
    product_details_page.check_visibility_of_product_details()
    for _ in range(3):
        product_details_page.increase_quantity_by_arrow()
    product_details_page.add_to_cart()
    cart_page = product_details_page.view_cart()
    cart_page.check_number_of_items_in_cart(1)
    cart_page.check_product_quantity(4)


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.PRODUCTS,
    sub_suite="Positive Tests",
    title="Delete a product from the cart",
)
@pytest.mark.ui
def test_delete_product_from_cart(home_page):
    all_products_page = home_page.go_to_products_page()
    all_products_page.add_first_product()
    cart_page = all_products_page.open_cart()
    cart_page.delete_product()
    cart_page.check_card_is_empty()


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.PRODUCTS,
    sub_suite="Positive Tests",
    title="Add a review to a product",
)
@pytest.mark.ui
def test_add_review_on_product(home_page):
    all_products_page = home_page.go_to_products_page()
    product_page = all_products_page.open_first_product_details()
    product_page.check_visibility_of_review_header()
    product_page.add_review()
    product_page.assert_success_message("Thank you for your review.")


@report_case(
    parent_suite=AllureParentSuite.UI,
    suite=AllureSuiteName.PRODUCTS,
    sub_suite="Positive Tests",
    title="Add a recommended item to the cart",
)
@pytest.mark.ui
def test_add_recommended_item_to_cart(home_page):
    home_page.scroll_to_bottom()
    home_page.is_recommended_section_visible()
    home_page.add_first_recommended_to_cart()
    cart_page = home_page.click_view_cart_in_modal_window()
    cart_page.check_number_of_items_in_cart(1)
    cart_page.check_product_quantity(1)
