import requests


class CreateBooking:
    def send_request_for_create_booking(self, firstname, lastname, general_totalprice, general_additionalneeds):
        headers = {"Content-Type": "application/json", "Accept": "*/*"}
        body = {"firstname": firstname, "lastname": lastname, "totalprice": general_totalprice, "depositpaid": True,
                "bookingdates": {"checkin": "2024-06-07", "checkout": "2024-08-09"},
                "additionalneeds": general_additionalneeds}
        response = requests.post("https://restful-booker.herokuapp.com/booking", json=body, headers=headers)
        self.status = response.status_code
        self.response = response.json()
        return response

    def check_request_status_code(self):
        assert self.status == 200

    def check_booking_in_response_body(self):
        assert "booking" in self.response, "Тело ответа не содержит объект 'booking'"
        self.bookings = self.response["booking"]

    def check_lastname(self, expected_lastname):
        assert self.bookings["lastname"] == expected_lastname

    def check_additionalneeds(self, expected_additionalneeds):
        assert self.bookings["additionalneeds"] == expected_additionalneeds

        print(self.response)
