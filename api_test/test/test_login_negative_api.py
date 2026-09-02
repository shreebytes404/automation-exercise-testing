import requests


def test_verify_login_missing_email():
    response = requests.post(
        "https://automationexercise.com/api/verifyLogin",
        data={"password": "somepassword"}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["responseCode"] == 400
    assert "email or password parameter is missing" in data["message"]