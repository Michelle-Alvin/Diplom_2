import allure
import requests


@allure.epic("Модуль создания заявок")
class TestCreateOrder:
    @allure.title("Создание заявки авторизованным пользователем")
    def test_create_order_with_authorization(self, token):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa79", "61c0c5a71d1f82001bdaaa70",
                            "61c0c5a71d1f82001bdaaa7a"]
        }
        headers = {
            'Authorization': token
        }

        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=payload, headers=headers)

        assert response.status_code == 200

        response = response.json()
        ingredient_names = [ingredient['name'] for ingredient in response['order']['ingredients']]

        assert "Флюоресцентная булка R2-D3" in ingredient_names
        assert "Мини-салат Экзо-Плантаго" in ingredient_names
        assert "Говяжий метеорит (отбивная)" in ingredient_names
        assert "Сыр с астероидной плесенью" in ingredient_names
        assert response['order']['name'] == "Экзо-плантаго метеоритный флюоресцентный астероидный бургер"

    @allure.title("Создание заявки без авторизации")
    def test_create_order_without_authorization(self):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa79", "61c0c5a71d1f82001bdaaa70",
                            "61c0c5a71d1f82001bdaaa7a"]
        }

        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=payload)

        assert response.status_code == 200, "Ошибка создания заказа"

        response = response.json()

        assert response[
                   'name'] == "Экзо-плантаго метеоритный флюоресцентный астероидный бургер", f"'{response['name']}' вместо ожидаемого результата"
        assert response['order']['number']

    @allure.title("Создание заявки с ингредиентами")
    def test_create_order_with_ingredients(self):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa77", "61c0c5a71d1f82001bdaaa78"]
        }

        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=payload)

        assert response.status_code == 200, "Ошибка создания заказа"

        response = response.json()

        assert response['name'] == "Фалленианский альфа-сахаридный бургер"

    @allure.title("Создание заявки без ингредиентов")
    def test_create_order_withou_ingredients(self):
        payload = {
            "ingredients": []
        }

        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=payload)

        assert response.status_code == 400
        assert 'Ingredient ids must be provided' in response.text

    @allure.title("Создание заявки с некорректным хэшем ингридиента")
    def test_create_order_incorrect_ingredient_hash(self):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaaGG", "61c0c5a71d1f82001bdaaa78"]
        }

        response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=payload)

        assert response.status_code == 500
