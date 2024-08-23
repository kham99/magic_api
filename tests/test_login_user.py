from endpoints.login_user import LoginUser


def test_login_user_swagger(generate_username_swagger, generate_password_swagger):
    endpoint = LoginUser()
    endpoint.get_login_user(generate_username_swagger, generate_password_swagger)
    endpoint.check_status_code()
    endpoint.check_login()
