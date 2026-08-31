import time
from playwright.sync_api import Page
from ui_test.pages.login_page import LoginPage


def test_new_user_signup(page: Page):
    login_page = LoginPage(page)
    login_page.go_to_login_page()

    unique_email = f"testuser{int(time.time())}@example.com"
    login_page.signup_new_user("Test User", unique_email)

    login_page.fill_account_information(
        password="Test@1234",
        day="10",
        month="5",
        year="1998",
        first_name="Test",
        last_name="User",
        address="123 Test Street",
        state="West Bengal",
        city="Kolkata",
        zipcode="700001",
        mobile="9876543210"
    )

