import allure
import requests
from data.URL import Url


class TestGetListOfOders:
    @allure.title('Получение заказов авторизованного пользователя')
    @allure.step('Проверка получения заказов конкретного пользователя (код - 200 и текст "success" = True в ответе)')
    def test_create_user_success(self, create_new_user_and_avtorization):
        token = create_new_user_and_avtorization["token"]
        response = requests.get(Url.GET_LIST_OF_ORDERS, headers={'Authorization': token})
        assert response.status_code == 200
        assert response.json().get("success") == True, "Получен неверный ответ"


    @allure.title('Проверка получения заказа неавторизованным пользователем')
    @allure.step('Проверка получения заказов неавторизованным пользователем (код - 401 и текст "success"=False  в ответе)')
    def test_get_order_whithout_auth(self):
        response = requests.get(Url.GET_LIST_OF_ORDERS)
        assert response.status_code == 401
        assert response.json().get("success") == False, "Получен неверный ответ"