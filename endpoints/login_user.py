import requests


class LoginUser:
    def get_login_user(self, username, password):
        response = requests.get(f"https://petstore.swagger.io/v2/user/login?username={username}&password={password}")
        self.status_code = response.status_code
        self.response_body = response.json()

    def check_status_code(self):
        assert self.status_code == 200

    def check_login(self):
        assert "logged in user" in self.response_body['message']


