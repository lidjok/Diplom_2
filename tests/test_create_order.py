import allure
import requests
from data.URL import Url
from database import Ingredients


class TestCreateOrder:
    @allure.title('Создание заказа авторизованным пользователем')
    @allure.step('Проверка успешного создания заказа авторизованным пользователем (код - 200 и текст "success" = True в ответе)')

    def test_create_order_avtorization_user_success(self, create_new_user_and_avtorization):
        token = create_new_user_and_avtorization["token"]
        response = requests.post(Url.CREATE_ORDER, headers={'Authorization': token}, data=Ingredients.correct_list_of_ingredients)
        assert response.status_code == 200
        assert response.json()["success"] == True


    @allure.title('Создание заказа неавторизованного пользователя')
    @allure.step('Проверка успешного создания заказа неавторизованным пользователем (код - 200 и текст "success" = True в '
        'ответе)')
    def test_create_order_new_user_success(self):
        response = requests.post(Url.CREATE_ORDER, data=Ingredients.correct_list_of_ingredients)
        assert response.status_code == 200
        assert response.json()["success"] == True


    @allure.title('Невозможно создать заказ без ингридиентов')
    @allure.step('Проверка невозможности создать заказ без ингридиентов (код - 400 и текст "success" = False в '
        'ответе)')
    def test_create_order_without_ingredients(self, create_new_user_and_avtorization):
        token = create_new_user_and_avtorization["token"]
        response = requests.post(Url.CREATE_ORDER, headers={'Authorization': token},
                                 data=Ingredients.empty_list_of_ingredients)
        assert response.status_code == 400
        assert response.json()['message'] == 'Ingredient ids must be provided'


    @allure.title('Невозможно создать заказ c неверным хэшом ингедиентов')
    @allure.step('Проверка невозможности создать заказ передав ингредиенты с неверным хэщом ,код - 500 в ответе ')
    def test_create_order_with_wrong_hash(self, create_new_user_and_avtorization):
        token = create_new_user_and_avtorization["token"]
        response = requests.post(Url.CREATE_ORDER, headers={'Authorization': token},
                                 data=Ingredients.wrong_list_of_ingredients_incorrect_hash)
        assert response.status_code == 500
        assert response.reason == 'Internal Server Error'