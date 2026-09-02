import requests

TEST_EMAIL = "my_email@example.com"


def test_get_user_detail_by_email():
    response = requests.get(
        "https://automationexercise.com/api/getUserDetailByEmail",
        params={"email": TEST_EMAIL}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["responseCode"] == 200
    assert data["user"]["email"] == TEST_EMAIL