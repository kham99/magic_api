from endpoints.swagger_get_user import SwaggerGetUser
import pytest


@pytest.mark.swagger()
def test_swagger_getting_user():
    endpoint = SwaggerGetUser()
    endpoint.getting_user()
    endpoint.check_status_code()
    endpoint.check_username()
    endpoint.check_password()
