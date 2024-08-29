import allure
from endpoints.swagger_get_user import SwaggerGetUser


@allure.title("Get user by username")
@allure.feature("Tests Swagger")
@allure.story('Get')
def test_swagger_getting_user():
    endpoint = SwaggerGetUser()
    endpoint.getting_user()
    endpoint.check_username()
