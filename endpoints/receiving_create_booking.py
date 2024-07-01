import requests


class ReceiveBooking:

    def get_create_booking(self, book_id):
        headers = {"Content-Type": "application/json", "Accept": "*/*"}
        response = requests.get(f"https://restful-booker.herokuapp.com/booking/{book_id}", headers=headers)
        self.status = response.status_code
        self.response = response.json()
        return self.response

    def check_request_status_code(self):
        assert self.status == 200

    def check_firstname(self):
        assert len(self.response["firstname"]) > 0

    def check_totalprice(self):
        assert self.response["totalprice"] > 0

        print(self.response)

