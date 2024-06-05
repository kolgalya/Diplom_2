from burger_api import BurgerApi
import allure
import help
import data

class TestChangeUser:
    @allure.description('Успешное изменение почты авторизованного пользователя')
    def test_can_change_login_authorization_user(self, create_user_fixture):
        user, user_data = create_user_fixture
        authorized_user = BurgerApi.login_user(user_data)
        user_data['email'] = help.generate_random_string(3) + '@mail.ru'
        change = BurgerApi.change_user(authorized_user.json()['accessToken'], user_data)
        assert change.status_code == 200 and change.json()["success"] == True

    @allure.description('Успешное изменение пароля авторизованного пользователя')
    def test_can_change_password_authorization_user(self, create_user_fixture):
        user, user_data = create_user_fixture
        authorized_user = BurgerApi.login_user(user_data)
        user_data['password'] = help.generate_random_string(6)
        change = BurgerApi.change_user(authorized_user.json()['accessToken'], user_data)
        assert change.status_code == 200 and change.json()["success"] == True

    @allure.description('Успешное изменение имени авторизованного пользователя')
    def test_can_change_name_authorization_user(self, create_user_fixture):
        user, user_data = create_user_fixture
        authorized_user = BurgerApi.login_user(user_data)
        user_data['name'] = help.generate_random_string(4)
        change = BurgerApi.change_user(authorized_user.json()['accessToken'], user_data)
        assert change.status_code == 200 and change.json()["success"] == True

    @allure.description('Нельзя изменить почту на уже используемую у авторизованного пользователя')
    def test_can_not_change_login_existing_mail_authorization_user(self, create_user_fixture):
        user, user_data = create_user_fixture
        authorized_user = BurgerApi.login_user(user_data)
        user_data['email'] = data.existing_user_body['email']
        change = BurgerApi.change_user(authorized_user.json()['accessToken'], user_data)
        assert change.status_code == 403 and change.json()["success"] == False

    @allure.description('Нельзя изменить почту неавторизованного пользователя')
    def test_can_not_change_login_not_authorization_user(self, create_user_fixture):
        user, user_data = create_user_fixture
        user_data['email'] = help.generate_random_string(3) + '@mail.ru'
        change = BurgerApi.change_user(user.json()['accessToken'], user_data)
        assert change.status_code == 401 and change.json()["success"] == False

    @allure.description('Нельзя изменить пароль неавторизованного пользователя')
    def test_can_not_change_password_not_authorization_user(self, create_user_fixture):
        user, user_data = create_user_fixture
        user_data['password'] = help.generate_random_string(6)
        change = BurgerApi.change_user(user.json()['accessToken'], user_data)
        assert change.status_code == 401 and change.json()["success"] == False

    @allure.description('Нельзя изменить имя неавторизованного пользователя')
    def test_can_not_change_name_not_authorization_user(self, create_user_fixture):
        user, user_data = create_user_fixture
        user_data['name'] = help.generate_random_string(4)
        change = BurgerApi.change_user(user.json()['accessToken'], user_data)
        assert change.status_code == 401 and change.json()["success"] == False

    @allure.description('Нельзя изменить почту на уже используемую у неавторизованного пользователя')
    def test_can_not_change_login_existing_mail_not_authorization_user(self, create_user_fixture):
        user, user_data = create_user_fixture
        user_data['email'] = data.existing_user_body['email']
        change = BurgerApi.change_user(user.json()['accessToken'], user_data)
        assert change.status_code == 403 and change.json()["success"] == False