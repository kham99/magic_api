import requests


class ReceiveToken:
    status = None
    token = None

    def send_request_for_authorization(self):
        response = requests.post("https://restful-booker.herokuapp.com/auth",
                                 json={"username": "admin", "password": "password123"},
                                 headers={"Content-Type": "application/json"})
        self.status = response.status_code
        self.token = response.json()["token"]
        return response

    def check_response_status_is_ok(self):
        assert self.status == 200

    def check_token_in_response(self):
        assert len(self.token) > 0
