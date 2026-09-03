# Automation Exercise – UI & API Test Automation Framework

A Python test automation framework for [automationexercise.com](https://automationexercise.com), covering both UI (Playwright) and API (Requests) layers, built using the Page Object Model design pattern, with a fully automated CI/CD pipeline via GitHub Actions.

## What's Tested

**UI (Playwright) — 9 tests**
- **Signup** – Multi-page new user registration flow
- **Login** – 5 test cases: successful login, wrong password, unregistered email, empty email, empty password
- **Product Search** – Verifies search results actually match the search term
- **Add to Cart** – Dynamically verifies the correct product lands in the cart
- **Checkout** – Full end-to-end flow: login → add to cart → checkout → payment → order confirmation

**API (Requests) — 9 tests**
- **Products List** (GET) – Validates response structure and product field formats
- **Search Product** (POST) – Validates results with a match-ratio assertion, accounting for the API's category-based matching
- **Search Product – Missing Parameter** (negative) – Validates the 400 error response
- **Verify Login** – Valid credentials, missing email (negative), invalid credentials (negative)
- **Verify Login – Wrong HTTP Method** (negative) – Validates the 405 error when using DELETE instead of POST
- **Create Account** (POST) – Registers a new user with a unique, timestamp-based email
- **Get User Detail by Email** (GET) – Validates nested JSON fields against a known account

## Tech Stack

- Python
- Playwright
- Requests
- pytest
- Page Object Model (POM) design pattern
- GitHub Actions (CI/CD)

## Project Structure

ui_test/
├── pages/ # Page objects – one file per site page
│ ├── login_page.py
│ ├── product_page.py
│ ├── cart_page.py
│ └── checkout_page.py
├── tests/ # UI test files
│ ├── test_signup.py
│ ├── test_login.py
│ ├── test_search_product.py
│ ├── test_cart.py
│ └── test_checkout.py
└── test_sanity.py

api_test/
└── test/ # API test files
├── test_products_api.py
├── test_search_product_api.py
├── test_search_product_negative_api.py
├── test_login_api.py
├── test_login_negative_api.py
├── test_login_wrong_method_api.py
├── test_create_account_api.py
└── test_get_user_detail_api.py

.github/
└── workflows/
└── tests.yml # CI/CD pipeline – runs both suites on every push


## How to Run

```bash
git clone https://github.com/shreebytes404/automation-exercise-testing.git
cd automation-exercise-testing
pip install pytest-playwright requests
playwright install
pytest ui_test/tests/ --headed
pytest api_test/test/
```

## CI/CD

Both the UI and API test suites run automatically on every push via GitHub Actions — see `.github/workflows/tests.yml`.

## Challenges Solved

Real issues hit and debugged while building this framework:

- **Race condition on signup assertion** – Initial assert checked page content immediately after form submission, before navigation completed, causing a false failure. Fixed using `wait_for_selector` to wait for the actual confirmation element instead of checking instantly.
- **Ambiguous locator (Playwright strict mode violation)** – A "View Cart" locator matched both a popup link and the navbar link, so Playwright refused to click. Fixed by scoping the locator to search only within the popup's container.
- **Module import errors** – Test files couldn't import page objects due to missing `__init__.py` files, which Python needs to recognize folders as importable packages.
- **Git tracking `.idea`/`__pycache__` despite `.gitignore`** – These had already been tracked before `.gitignore` was added, so they kept appearing in the repo. Fixed with `git rm -r --cached` to untrack them without deleting them locally.
- **CI-only flaky checkout test** – A test that passed locally failed in GitHub Actions with a timeout, because the CI environment's page load was slower than expected. Fixed by explicitly waiting for the payment page's first field to appear before interacting with it, instead of relying on default timing.
- **API documentation mismatch** – The API's own docs stated certain endpoints return specific HTTP status codes (e.g. 404, 405), but the actual HTTP response was always 200, with the real result code embedded inside the JSON body. Verified this behavior manually before writing assertions, rather than trusting the docs blindly.