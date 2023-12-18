import allure
import requests


@allure.epic("Модуль регистрации пользователя")
class TestEditUser:
    @allure.title("Редактирование пользователя")
    def test_edit_user_with_authorization(self, token):
        # Выполняем авторизацию для получения токена
        headers = {
            'Authorization': token
        }

        # Проверяем текущее значение поля "name", которое будем редактировать
        response = requests.get('https://stellarburgers.nomoreparties.site/api/auth/user', headers=headers)

        assert response.json()["user"]["name"] == "arseniy1"

        # Редактируем поле "name"
        payload = {
            "name": "arseniy2"
        }

        response = requests.patch(' https://stellarburgers.nomoreparties.site/api/auth/user',
                                  headers=headers, json=payload)

        assert response.json()["user"]["name"] == "arseniy2"
        assert response.json()["user"]["email"] == "arseniy1@yandex.ru"

        # Возращаем исходное значение "name"
        payload = {
            "name": "arseniy1"
        }

        response = requests.patch(' https://stellarburgers.nomoreparties.site/api/auth/user',
                                  headers=headers, json=payload)

        assert response.json()["user"]["name"] == "arseniy1"

    @allure.title("Редактирование без авторизации")
    def test_edit_user_without_token(self):
        payload = {
            "name": "new_name",
        }
        response = requests.patch(' https://stellarburgers.nomoreparties.site/api/auth/user', json=payload)

        assert response.status_code == 401
        assert 'You should be authorised' in response.text
