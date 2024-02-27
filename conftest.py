import requests
import pytest


@pytest.fixture(scope='function')
def token():
    payload = {
        "email": "arseniy1@yandex.ru",
        "password": "123456"
    }
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', json=payload)
    token = response.json()['accessToken']
    return token
