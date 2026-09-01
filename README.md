# Automation Exercise – Playwright Test Framework

A Python + Playwright test automation framework for [automationexercise.com](https://automationexercise.com), built using the Page Object Model design pattern. Covers core e-commerce UI flows with both positive and negative test scenarios.

## What's Tested

- **Signup** – Multi-page new user registration flow
- **Login** – 5 test cases: successful login, wrong password, unregistered email, empty email, empty password
- **Product Search** – Verifies search results actually match the search term
- **Add to Cart** – Dynamically verifies the correct product lands in the cart
- **Checkout** – Full end-to-end flow: login → add to cart → checkout → payment → order confirmation

## Tech Stack

- Python
- Playwright
- pytest
- Page Object Model (POM) design pattern

## Project Structure
ui_test/
├── pages/ # Page objects – one file per site page
│ ├── login_page.py
│ ├── product_page.py
│ ├── cart_page.py
│ └── checkout_page.py
├── tests/ # Test files
│ ├── test_signup.py
│ ├── test_login.py
│ ├── test_search_product.py
│ ├── test_cart.py
│ └── test_checkout.py
└── test_sanity.py


## How to Run

```bash
git clone https://github.com/shreebytes404/automation-exercise-testing.git
cd automation-exercise-testing
pip install pytest-playwright
playwright install
pytest ui_test/tests/ --headed
```

## Challenges Solved

Real issues hit and debugged while building this framework:

- **Race condition on signup assertion** – Initial assert checked page content immediately after form submission, before navigation completed, causing a false failure. Fixed using `wait_for_selector` to wait for the actual confirmation element instead of checking instantly.
- **Ambiguous locator (Playwright strict mode violation)** – A "View Cart" locator matched both a popup link and the navbar link, so Playwright refused to click. Fixed by scoping the locator to search only within the popup's container.
- **Module import errors** – Test files couldn't import page objects due to missing `__init__.py` files, which Python needs to recognize folders as importable packages.
- **Git tracking `.idea` despite `.gitignore`** – IDE config folder had already been tracked before `.gitignore` was added, so it kept appearing in the repo. Fixed with `git rm -r --cached` to untrack it without deleting it locally.

## Upcoming

- API test suite (`api_tests/`)
- GitHub Actions CI/CD pipeline