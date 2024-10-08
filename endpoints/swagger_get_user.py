import requests
from clients.http_client import HTTPClient


class SwaggerGetUser(HTTPClient):

    def __init__(self):
        self._http_client_ = HTTPClient()

    def getting_user(self):
        response = self._send_request(url="https://petstore.swagger.io/v2/user/kham99",
                                      method="get",
                                      expected_status_code=200
                                      )
        self.status_code = response.status_code
        self.response_body = response.json()
        print(response)

    def check_username(self):
        assert self.response_body["username"] == "kham99"
