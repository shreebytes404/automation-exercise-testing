import requests


def test_get_products_list():
    response = requests.get("https://automationexercise.com/api/productsList")

    assert response.status_code == 200
    data = response.json()
    assert data["responseCode"] == 200
    assert len(data["products"]) > 0

    first_product = data["products"][0]
    assert "id" in first_product
    assert "name" in first_product
    assert "price" in first_product
    assert first_product["price"].startswith("Rs.")