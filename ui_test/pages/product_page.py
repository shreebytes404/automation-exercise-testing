from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator('#search_product')
        self.search_button = page.locator('#submit_search')


    def go_to_products_page(self):
        self.page.goto("https://automationexercise.com/products")

    def search_product(self, product_name: str):
        self.search_input.fill(product_name)
        self.search_button.click()

    def test_search_product(page: Page):
        product_page = ProductPage(page)
        product_page.go_to_products_page()

        product_page.search_product("top")

        page.wait_for_selector("text=SEARCHED PRODUCTS")

        product_names = product_page.get_all_result_product_names()
        assert len(product_names) > 0
        for name in product_names:
            assert "top" in name.lower()

    def add_first_product_to_cart(self):
        product_name = self.page.locator('.productinfo p').first.inner_text()
        self.page.locator('.add-to-cart').first.hover()
        self.page.locator('.add-to-cart').first.click()
        return product_name