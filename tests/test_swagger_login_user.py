import allure
from endpoints.swagger_login_user import LoginUser


@allure.title("Logs user into to system")
@allure.feature("Tests Swagger")
@allure.story('Get')
def test_login_user_swagger(generate_username_swagger, generate_password_swagger):
    endpoint = LoginUser()
    endpoint.get_login_user(generate_username_swagger, generate_password_swagger)
    endpoint.check_login()
