import allure
import requests
from data.URL import Url
from helpers import generation_new_data_user


class TestLoginUser:
    @allure.title('Авторизация пользователя')
    @allure.step('Проверка авторизации ранее созданного пользователя (код - 200 и текст "success"=True в ответе)')
    def test_login_user_success(self, create_new_user):
        payload, _ = create_new_user
        response = requests.post(Url.LOGIN_USER, data=payload)
        assert response.status_code == 200
        assert response.json().get("success") == True, "Получен неверный ответ"


    @allure.title('Невозможно авторизоваться незарегестрированному пользователю')
    @allure.step('Проверка невозможности авторизоваться с ранее не зарегестрированными данными пользователя(код - 401 и текст "success"=False в ответе)')
    def test_login_user_unauthorized_error(self):
        data = generation_new_data_user()
        payload = data
        response = requests.post(Url.LOGIN_USER, data=payload)
        assert response.status_code == 401
        assert response.json()['message'] == 'email or password are incorrect'