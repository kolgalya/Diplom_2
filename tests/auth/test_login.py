import pytest
from burger_api import BurgerApi
import allure

class TestLoginUser:
    @allure.description('Успешная авторизация существующего пользователя')
    def test_can_login_user(self, create_user_fixture):
        user_data = create_user_fixture[1]
        authorized_user = BurgerApi.login_user(user_data)
        assert authorized_user.status_code == 200 and authorized_user.json()["success"] == True

    @allure.description('Нельзя авторизаваться с неверным логином')
    @pytest.mark.parametrize('email', ['new_email@mail.ru', ''])
    def test_can_not_incorrect_login_user(self, create_user_fixture, email):
        user_data = create_user_fixture[1]
        user_data['email'] = email
        authorized_user = BurgerApi.login_user(user_data)
        assert authorized_user.status_code == 401 and authorized_user.json()["success"] == False and authorized_user.json()["message"] == 'email or password are incorrect'

    @allure.description('Нельзя авторизаваться с неверным паролем')
    @pytest.mark.parametrize('password', ['password', ''])
    def test_can_not_incorrect_login_password(self, create_user_fixture, password):
        user_data = create_user_fixture[1]
        user_data['password'] = password
        authorized_user = BurgerApi.login_user(user_data)
        assert authorized_user.status_code == 401 and authorized_user.json()["success"] == False and authorized_user.json()["message"] == 'email or password are incorrect'


