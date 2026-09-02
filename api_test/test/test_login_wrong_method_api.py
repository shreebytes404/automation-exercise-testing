import requests


def test_verify_login_wrong_method():
    response = requests.delete("https://automationexercise.com/api/verifyLogin")

    assert response.status_code == 200

    data = response.json()
    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."