import pytest
import data
from burger_api import BurgerApi
import allure

class TestOrders:
    @allure.description('Успешное создание заказа авторизованным пользователем')
    def test_can_make_order_authorization_user(self, create_user_fixture):
        user_data = create_user_fixture[1]
        authorized_user = BurgerApi.login_user(user_data)
        order = BurgerApi.create_order(data.right_order)
        assert order.status_code == 200 and order.json()["success"] == True

    @allure.description('Нельзя создать заказ неавторизованным пользователем')
    def test_can_not_make_order_not_authorization_user(self, create_user_fixture):
        user = create_user_fixture[0]
        order = BurgerApi.create_order(data.right_order)
        assert order.status_code == 400 and order.json()["success"] == False

    @allure.description('Нельзя создать заказ без ингредиентов')
    def test_can_not_make_order_not_authorization_user(self, create_user_fixture):
        user_data = create_user_fixture[1]
        authorized_user = BurgerApi.login_user(user_data)
        order = BurgerApi.create_order(data.empty_order)
        assert order.status_code == 400 and order.json()["success"] == False and order.json()["message"] == 'Ingredient ids must be provided'

    @allure.description('Нельзя создать заказ c некорректными ингредиентами')
    @pytest.mark.parametrize('wrong_id', ['61c0c5a71d1f82001bdaaa1d', '000000000000000000000000', '007b', 'c'])
    def test_can_not_wrong_order_authorization_user(self, create_user_fixture, wrong_id):
        user_data = create_user_fixture[1]
        authorized_user = BurgerApi.login_user(user_data)
        wrong_order = {"ingredients": wrong_id}
        order = BurgerApi.create_order(wrong_order)
        assert order.status_code == 500

    @allure.description('Успешное получение списка заказов авторизованного пользователя')
    def test_can_get_list_order_authorization_user(self, create_user_fixture):
        user_data = create_user_fixture[1]
        authorized_user = BurgerApi.login_user(user_data)
        order = BurgerApi.create_order(data.empty_order)
        order_list_user = BurgerApi.order_list(authorized_user.json()['accessToken'])
        assert order_list_user.status_code == 200 and order_list_user.json()["success"] == True

    @allure.description('Нельзя получить список заказов неавторизованного пользователя')
    def test_can_not_get_list_order_not_authorization_user(self, create_user_fixture):
        user = create_user_fixture[0]
        order_list_user = BurgerApi.order_list(None)
        assert order_list_user.status_code == 401 and order_list_user.json()["success"] == False and order_list_user.json()["message"] == 'You should be authorised'
