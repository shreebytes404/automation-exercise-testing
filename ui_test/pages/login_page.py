from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Signup section (first page)
        self.name_input = page.locator('[data-qa="signup-name"]')
        self.email_input = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.locator('[data-qa="signup-button"]')

        # Account information page (second page)
        self.password_input = page.locator('[data-qa="password"]')
        self.day_dropdown = page.locator('[data-qa="days"]')
        self.month_dropdown = page.locator('[data-qa="months"]')
        self.year_dropdown = page.locator('[data-qa="years"]')
        self.first_name_input = page.locator('[data-qa="first_name"]')
        self.last_name_input = page.locator('[data-qa="last_name"]')
        self.address_input = page.locator('[data-qa="address"]')
        self.state_input = page.locator('[data-qa="state"]')
        self.city_input = page.locator('[data-qa="city"]')
        self.zipcode_input = page.locator('[data-qa="zipcode"]')
        self.mobile_input = page.locator('[data-qa="mobile_number"]')
        self.create_account_button = page.locator('[data-qa="create-account"]')

        # Login section
        self.login_email_input = page.locator('[data-qa="login-email"]')
        self.login_password_input = page.locator('[data-qa="login-password"]')
        self.login_button = page.locator('[data-qa="login-button"]')

    def go_to_login_page(self):
        self.page.goto("https://automationexercise.com/login")

    def signup_new_user(self, name: str, email: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()

    def fill_account_information(self, password, day, month, year, first_name,
                                   last_name, address, state, city, zipcode, mobile):
        self.password_input.fill(password)
        self.day_dropdown.select_option(day)
        self.month_dropdown.select_option(month)
        self.year_dropdown.select_option(year)
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.address_input.fill(address)
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zipcode)
        self.mobile_input.fill(mobile)
        self.create_account_button.click()

    def login(self, email: str, password: str):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()