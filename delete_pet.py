import requests
import pytest


def test_delete_petstore():
    url = "https://petstore.swagger.io/v2/pet/1"

    response = requests.delete(url)