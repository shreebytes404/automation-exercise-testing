from playwright.sync_api import Page
from ui_test.pages.login_page import LoginPage
from ui_test.pages.product_page import ProductPage
from ui_test.pages.cart_page import CartPage
from ui_test.pages.checkout_page import CheckoutPage

TEST_EMAIL = "my_email@example.com"
TEST_PASSWORD = "Test@1234"


def test_full_checkout_flow(page: Page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Step 1: Login
    login_page.go_to_login_page()
    login_page.login(email=TEST_EMAIL, password=TEST_PASSWORD)
    page.wait_for_selector("text=Logged in as")

    # Step 2: Add product to cart
    product_page.go_to_products_page()
    product_page.add_first_product_to_cart()
    cart_page.go_to_cart()

    # Step 3: Checkout
    checkout_page.proceed_to_checkout()
    checkout_page.place_order()

    # Step 4: Payment
    checkout_page.fill_payment_details()
    checkout_page.confirm_payment()

    # Step 5: Verify order placed
    page.wait_for_selector("text=Order Placed!")
    assert page.locator("text=Order Placed!").is_visible()