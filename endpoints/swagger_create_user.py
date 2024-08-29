from clients.http_client import HTTPClient


class CreateUser(HTTPClient):

    def __init__(self):
        self._http_client = HTTPClient()

    def create_new_user(self, id, password, lastname, firstname, email, phone):
        body = [
  {
    "id": id,
    "username": "kham99",
    "firstName": firstname,
    "lastName": lastname,
    "email": email,
    "password": password,
    "phone": phone,
    "userStatus": 0
  }
]
        response = self._send_request(url="https://petstore.swagger.io/v2/user/createWithList",
                                      json=body,
                                      method="post",
                                      expected_status_code=200)
        self.response = response.json()
        self.code = response.status_code
        print(self.response)