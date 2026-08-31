from playwright.sync_api import Page
from ui_test.pages.login_page import LoginPage

TEST_EMAIL = "my_email@example.com"
TEST_PASSWORD = "Test@1234"


def test_existing_user_login(page: Page):
    login_page = LoginPage(page)
    login_page.go_to_login_page()

    login_page.login(email=TEST_EMAIL, password=TEST_PASSWORD)

    page.wait_for_selector("text=Logged in as")
    assert page.locator("text=Logged in as").is_visible()

#TEST-CASE 1
def test_login_wrong_password(page: Page):
    login_page = LoginPage(page)
    login_page.go_to_login_page()

    login_page.login(email=TEST_EMAIL, password="WrongPassword123")

    page.wait_for_selector("text=Your email or password is incorrect!")
    assert page.locator("text=Your email or password is incorrect!").is_visible()


#TEST CASE 2
def test_login_unregistered_email(page: Page):
    login_page = LoginPage(page)
    login_page.go_to_login_page()

    login_page.login(email="doesnotexist99999@example.com", password="AnyPassword123")

    page.wait_for_selector("text=Your email or password is incorrect!")
    assert page.locator("text=Your email or password is incorrect!").is_visible()

#testcase 3

def test_login_empty_email(page: Page):
    login_page = LoginPage(page)
    login_page.go_to_login_page()

    login_page.login(email="", password=TEST_PASSWORD)

    validation_message = login_page.login_email_input.evaluate(
        "el => el.validationMessage"
    )
    assert validation_message != ""
    assert page.url.endswith("/login")  # form did NOT submit, still on login page

#testcase 4
def test_login_empty_password(page: Page):
    login_page = LoginPage(page)
    login_page.go_to_login_page()

    login_page.login(email=TEST_EMAIL, password="")

    validation_message = login_page.login_password_input.evaluate(
        "el => el.validationMessage"
    )
    assert validation_message != ""
    assert page.url.endswith("/login")  # form did NOT submit, still on login page