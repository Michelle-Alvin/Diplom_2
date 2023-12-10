import allure
import requests


@allure.title("Модуль авторизации пользователя")
class TestLoginUser:
    @allure.title("Корректная авторизация")
    def test_login_user(self):
        payload = {
            "email": "arseniy1@yandex.ru",
            "password": "123456"
        }

        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=payload)

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title("Авторизация с некорректным паролем")
    def test_login_user_with_invalid_password(self):
        payload = {
            "email": "arseniy1@yandex.ru",
            "password": "654321"
        }

        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=payload)

        assert response.status_code == 401
        assert 'email or password are incorrect' in response.text
