from playwright.sync_api import Page
from ui_test.pages.product_page import ProductPage


def test_search_product(page: Page):
    product_page = ProductPage(page)
    product_page.go_to_products_page()

    product_page.search_product("top")

    page.wait_for_selector("text=SEARCHED PRODUCTS")
    assert page.locator("text=SEARCHED PRODUCTS").is_visible()