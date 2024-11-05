import allure
import requests
from data.URL import Url



class TestCreateUser:
    @allure.title('Создание пользователя')
    @allure.step('Проверка создания курьера (код - 200 и текст "success" = True в ответе)')
    def test_create_user_success(self, create_new_user):
        payload, response = create_new_user

        assert response.status_code == 200
        assert response.json().get("success") == True, "Получен неверный ответ"


    @allure.title('Проверка невозможности создания Пользователя с ранее зарегестрированными данными')
    @allure.step('Проверка невозможности создания Пользователя с дублирующими данными (код - 403 и текст "message": "User already exists" в ответе)')
    def test_create_user_doub_data_error(self, create_new_user):
        payload, _ = create_new_user
        response_doub_register = requests.post(Url.CREATE_USER, data=payload)
        assert response_doub_register.status_code == 403
        assert response_doub_register.json().get("message") == "User already exists", "Ошибка: неверное сообщение."


    @allure.title('Проверка невозможности создания Пользователя без обязательных данных')
    @allure.step('Проверка невозможности создания Пользователя без Password (код - 403 и текст "message": "Email, password and name are required fields" в ответе)')
    def test_create_user_without_password(self, create_user_without_password):
        payload = create_user_without_password
        response = requests.post(Url.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.json().get("message") == "Email, password and name are required fields", "Ошибка: неверное сообщение."