import requests


def test_search_product():
    response = requests.post(
        "https://automationexercise.com/api/searchProduct",
        data={"search_product": "top"}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["responseCode"] == 200
    assert len(data["products"]) > 0

    matching = [p for p in data["products"] if "top" in p["name"].lower()]
    match_ratio = len(matching) / len(data["products"])
    assert match_ratio > 0.5