import requests


class SwaggerGetUser:
    def getting_user(self):
        response = requests.get("https://petstore.swagger.io/v2/user/kham99")
        self.status_code = response.status_code
        self.response_body = response.json()

    def check_status_code(self):
        assert self.status_code == 200

    def check_username(self):
        assert self.response_body["username"] == "kham99"


