import allure
import pytest
import requests
from helpers import generation_new_data_user_and_avtorization
from helpers import generation_new_data_user
from data.URL import Url


@pytest.fixture
def create_new_user():
    payload = generation_new_data_user()
    response = requests.post(Url.CREATE_USER, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(Url.DELETE_USER, headers={"Authorization": token})


@pytest.fixture
def create_user_without_password():
    payload = generation_new_data_user()
    payload.pop("password", None)
    return payload


@pytest.fixture
def create_new_user_and_avtorization():
    result = generation_new_data_user_and_avtorization()
    yield result
    token = result["token"]
    requests.delete(Url.DELETE_USER, headers={"Authorization": token})


