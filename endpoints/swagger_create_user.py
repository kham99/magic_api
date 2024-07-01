import requests


class CreateUser():
    def create_new_user(self, password):
        headers = {"Accept": "*/*", "accept": "application/json"}
        body = [
  {
    "id": 99,
    "username": "kham99",
    "firstName": "Amir",
    "lastName": "Khabiev",
    "email": "netu@yandex.ru",
    "password": password,
    "phone": "8999999999",
    "userStatus": 0
  }
]
        response = requests.post("https://petstore.swagger.io/v2/user/createWithList", headers=headers, json=body)
        self.response = response.json()
        self.code = response.status_code

    def check_status_code(self):
        assert self.code == 200
