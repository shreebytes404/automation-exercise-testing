import requests
import time


def test_create_account():
    unique_email = f"apitestuser{int(time.time())}@example.com"

    response = requests.post(
        "https://automationexercise.com/api/createAccount",
        data={
            "name": "API Test User",
            "email": unique_email,
            "password": "Test@1234",
            "title": "Mr",
            "birth_date": "10",
            "birth_month": "5",
            "birth_year": "1998",
            "firstname": "API",
            "lastname": "Tester",
            "company": "TestCo",
            "address1": "123 Test Street",
            "address2": "",
            "country": "India",
            "zipcode": "700001",
            "state": "West Bengal",
            "city": "Kolkata",
            "mobile_number": "9876543210"
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert data["responseCode"] == 201
    assert data["message"] == "User created!"