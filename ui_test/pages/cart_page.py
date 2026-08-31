from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.view_cart_link = page.locator('#cartModal a[href="/view_cart"]')
        self.cart_product_links = page.locator('a[href^="/product_details/"]')

    def go_to_cart(self):
        self.view_cart_link.click()

    def get_product_names_in_cart(self):
        return self.cart_product_links.all_inner_texts()