import pytest
import allure
import help
from burger_api import BurgerApi

@allure.step('Создание пользователя и удаление его после теста')
@pytest.fixture
def create_user_fixture():
    email = help.generate_random_string(5) + '@mail.ru'
    password = help.generate_random_string(5)
    name = help.generate_random_string(5)
    user_data = {
        "email": email,
        "password": password,
        "name": name
    }
    user = BurgerApi.create_user(user_data)  # Создание пользователя
    yield user, user_data
    delete = BurgerApi.delete_user(user.json()['accessToken']) # Удаление пользователя

@allure.step('Создание регистрационных данных пользователя')
@pytest.fixture
def create_body_user_fixture():
    email = help.generate_random_string(5) + '@mail.ru'
    password = help.generate_random_string(5)
    name = help.generate_random_string(5)
    user_data = {
        "email": email,
        "password": password,
        "name": name
    }
    return user_data