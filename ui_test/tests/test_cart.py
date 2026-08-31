from playwright.sync_api import Page
from ui_test.pages.product_page import ProductPage
from ui_test.pages.cart_page import CartPage


def test_add_product_to_cart(page: Page):
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    product_page.go_to_products_page()
    added_product_name = product_page.add_first_product_to_cart()
    cart_page.go_to_cart()

    page.wait_for_selector("text=Shopping Cart")
    cart_products = cart_page.get_product_names_in_cart()
    assert added_product_name in cart_products