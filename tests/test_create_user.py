import allure
import requests

import user_genarate


@allure.title("Модуль регистрации пользователя")
class TestCreateUser:
    @allure.title("Регистрация нового пользователя")
    def test_register_user(self):
        payload = user_genarate.generate_json_body_new_user()
        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=payload)

        assert response.status_code == 200

        data = response.json()
        assert data['accessToken'], "Токена нет в ответе"

    @allure.title("Регистрация уже существующего пользователя")
    def test_register_already_registered(self):
        credentials = user_genarate.register_new_user_and_return_email_password()

        assert len(credentials) != 0, "Ошибка регистрации"

        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=credentials)

        assert response.status_code == 403, "Ошибка регистрации не воспроизвелась"
        assert 'User already exists' in response.text

    @allure.title("Регистрация с неполным набором обязательных полей")
    def test_register_missing_name(self):
        payload = {
            "email": user_genarate.generate_random_string(10),
            "password": user_genarate.generate_random_string(10)
        }

        response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=payload)

        assert response.status_code == 403, "Ошибка регистрации не воспроизвелась"
        assert 'Email, password and name are required fields' in response.text
