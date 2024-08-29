import allure
from endpoints.swagger_create_user import CreateUser


@allure.title("Create a new user")
@allure.feature("Tests Swagger")
@allure.story('Post')
def test_new_user_create(send_book_id, password_swagger, generate_lastname,
                         generate_firstname, generate_email, generate_phone):
    endpoint = CreateUser()
    endpoint.create_new_user(send_book_id, password_swagger, generate_lastname,
                             generate_firstname, generate_email, generate_phone)