from burger_api import BurgerApi
import allure
import data

class TestCreateUser:
    @allure.description('Уникального пользователя можно создать')
    def test_can_create_new_user(self, create_user_fixture):
        user = create_user_fixture[0]
        assert user.status_code == 200 and user.json()["success"] == True

    @allure.description('Нельзя создать пользователя, который уже существует')
    def test_can_not_create_existing_user(self):
        user = BurgerApi.create_user(data.existing_user_body)
        assert user.status_code == 403 and user.json()["success"] == False

    @allure.description('Нельзя создать пользователя без почты')
    def test_can_not_create_new_user_without_mail(self, create_user_fixture):
        user_body = create_user_fixture[1]
        user_body["email"] = ''
        user = BurgerApi.create_user(user_body)
        assert user.status_code == 403 and user.json()["success"] == False and user.json()["message"] == "Email, password and name are required fields"

    @allure.description('Нельзя создать пользователя без пароля')
    def test_can_not_create_new_user_without_password(self, create_user_fixture):
        user_body = create_user_fixture[1]
        user_body["password"] = ''
        user = BurgerApi.create_user(user_body)
        assert user.status_code == 403 and user.json()["success"] == False and user.json()["message"] == "Email, password and name are required fields"

