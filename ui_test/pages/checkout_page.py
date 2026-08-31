from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.proceed_to_checkout_button = page.locator('.check_out')
        self.place_order_button = page.locator('a[href="/payment"]')
        self.name_on_card_input = page.locator('[data-qa="name-on-card"]')
        self.card_number_input = page.locator('[data-qa="card-number"]')
        self.cvc_input = page.locator('[data-qa="cvc"]')
        self.expiry_month_input = page.locator('[data-qa="expiry-month"]')
        self.expiry_year_input = page.locator('[data-qa="expiry-year"]')
        self.pay_button = page.locator('[data-qa="pay-button"]')

    def proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()

    def place_order(self):
        self.place_order_button.click()

    def fill_payment_details(self, name="Test User", card_number="4111111111111111",
                              cvc="123", expiry_month="12", expiry_year="2027"):
        self.name_on_card_input.fill(name)
        self.card_number_input.fill(card_number)
        self.cvc_input.fill(cvc)
        self.expiry_month_input.fill(expiry_month)
        self.expiry_year_input.fill(expiry_year)

    def confirm_payment(self):
        self.pay_button.click()