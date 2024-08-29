from clients.http_client import HTTPClient


class ReceiveToken(HTTPClient):
    status = None
    token = None

    def __init__(self):
        self._http_client = HTTPClient()

    def _authorization(self):
        body = {"username": "admin", "password": "password123"}
        response = self._send_request(url="https://restful-booker.herokuapp.com/auth",
                                      method="post",
                                      json=body,
                                      expected_status_code=200
                                      )
        self.status = response.status_code
        self.token = response.json()["token"]
        return response

    def check_token_in_response(self):
        assert len(self.token) > 0
