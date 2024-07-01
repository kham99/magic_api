import requests


class ReceiveBooking:

    def get_create_booking(self):
        headers = {"Content-Type": "application/json", "Accept": "*/*"}
        response = requests.get(f"https://restful-booker.herokuapp.com/booking/9", headers=headers)
        self.status = response.status_code
        self.response = response.json()
        return self.response

    def check_request_status_code(self):
        assert self.status == 200


