import requests
import pytest


def test_post_petstore():
    url = "https://petstore.swagger.io/v2/pethttps://petstore.swagger.io/v2/pet"

    pet_data = {
        "id": 1,
        "name": "doggie",
        "status": "available"
    }

    response = requests.post(url, json=pet_data)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "Content-Type, api_key, Authorization"
    returned_pet = response.json()
    assert returned_pet["id"] == pet_data["id"]
    assert returned_pet["name"] == pet_data["name"]
    assert returned_pet["status"] == pet_data["status"]
    return returned_pet

