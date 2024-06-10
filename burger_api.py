import requests
import urls
import allure

class BurgerApi:
    @allure.step('Создание пользователя: POST /api/auth/register')
    def create_user(body):
        return requests.post(urls.BASE_URL + urls.CREATE_USER, json = body)

    @allure.step('Удаление пользователя: DELETE /api/auth/user')
    def delete_user(accessToken):
        return requests.delete(urls.BASE_URL + urls.DELETE_USER, headers ={"Authorization":accessToken})

    @allure.step('Авторизация пользователя: POST /api/auth/login')
    def login_user(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_USER, json = body)

    @allure.step('Изменение данных пользователя: PATCH /api/auth/user')
    def change_user(accessToken, body):
        return requests.patch(urls.BASE_URL + urls.CHANGE_USER, headers ={"Authorization":accessToken}, json = body)

    @allure.step('Создание заказа: POST /api/orders')
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER, json = body)

    @allure.step('Получение заказов конкретного пользователя: GET /api/orders')
    def order_list(accessToken):
        return requests.get(urls.BASE_URL + urls.ORDER_LIST_USER, headers ={"Authorization":accessToken})

