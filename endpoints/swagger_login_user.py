import requests
from clients.http_client import HTTPClient


class LoginUser(HTTPClient):
    def __init__(self):
        self._http_client_ = HTTPClient()

    def get_login_user(self, username, password):
        response = self._send_request(url=f"https://petstore.swagger.io/v2/user/login?username={username}"
                                          f"&password={password}",
                                      method="get",
                                      expected_status_code=200
                                      )
        self.status_code = response.status_code
        self.response_body = response.json()

    def check_login(self):
        assert "logged in user" in self.response_body['message']


