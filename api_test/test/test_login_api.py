import requests

TEST_EMAIL = "my_email@example.com"
TEST_PASSWORD = "Test@1234"


def test_verify_login_valid_credentials():
    response = requests.post(
        "https://automationexercise.com/api/verifyLogin",
        data={
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert data["responseCode"] == 200
    assert data["message"] == "User exists!"

def test_verify_login_invalid_credentials():
    response = requests.post(
        "https://automationexercise.com/api/verifyLogin",
        data={
            "email": "notarealuser99999@example.com",
            "password": "WrongPassword123"
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert data["responseCode"] == 404
    assert data["message"] == "User not found!"