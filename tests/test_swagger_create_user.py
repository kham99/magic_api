from endpoints.swagger_create_user import CreateUser
import pytest


@pytest.mark.swagger()
def test_new_user_create(password_swagger):
    endpoint = CreateUser()
    endpoint.create_new_user(password_swagger)
    endpoint.check_status_code()

