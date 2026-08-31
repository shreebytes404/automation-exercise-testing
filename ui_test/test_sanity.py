from playwright.sync_api import Page

def test_homepage_title(page: Page):
    page.goto("https://automationexercise.com")
    print(page.title())
    assert "Automation Exercise" in page.title()