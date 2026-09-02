import requests


def test_search_product_missing_parameter():
    response = requests.post("https://automationexercise.com/api/searchProduct")

    assert response.status_code == 200

    data = response.json()
    assert data["responseCode"] == 400
    assert "search_product parameter is missing" in data["message"]
