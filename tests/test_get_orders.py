import requests

import allure


@allure.epic("Модуль получения списка заявок")
class TestGetOrders:
    @allure.title("Получение списка заявок авторизованным пользователем")
    def test_get_orders_with_authorization(self, token):
        headers = {
            'Authorization': token
        }

        response = requests.get("https://stellarburgers.nomoreparties.site/api/orders", headers=headers)

        assert response.status_code == 200

        response = response.json()
        assert response['orders']

    @allure.title("Получение списка заявок без авторизации")
    def test_get_orders_without_authorization(self):
        response = requests.get("https://stellarburgers.nomoreparties.site/api/orders")

        assert response.status_code == 401
        assert 'You should be authorised' in response.text
