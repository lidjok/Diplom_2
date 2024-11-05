import allure
import requests
from data.URL import Url



class TestChangeUserData:

    @allure.title('Изменение данных авторизованного пользователя')
    @allure.step('Проверка изменения данных (Имени) авторизованного пользователя (код - 200 и текст "success"== True в ответе)')
    def test_change_authorized_user_name_success(self, create_new_user_and_avtorization):
        token = create_new_user_and_avtorization["token"]
        new_name = "NewTestName"
        response = requests.patch(Url.PACH_USER,
                                json={'name': new_name},
                                headers={'Authorization': token})

        assert response.status_code == 200
        assert response.json().get("success") == True

    @allure.title('Изменение данных неавторизованного пользователя')
    @allure.step(
        'Проверка невозможности изменения данных (Имени) неавторизованного пользователя (код - 401 и текст "message" == "You should be authorised")')
    def test_change_no_authorized_user_name_error(self, create_new_user):
            payload, _ = create_new_user
            new_name = "NewTestName"
            response = requests.patch(Url.PACH_USER,
                                  json={'name': new_name})
            assert response.status_code == 401
            assert response.json().get("message") == "You should be authorised"

