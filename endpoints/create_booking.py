from clients.http_client import HTTPClient


class Booking(HTTPClient):

    def __init__(self):
        self._http_client = HTTPClient()

    def _create_booking(self, firstname, lastname, general_totalprice, general_additionalneeds, checkin, checkout):
        body = {"firstname": firstname, "lastname": lastname, "totalprice": general_totalprice, "depositpaid": True,
                "bookingdates": {"checkin": checkin, "checkout": checkout},
                "additionalneeds": general_additionalneeds}

        response = self._send_request(url="https://restful-booker.herokuapp.com/booking",
                                      method="post",
                                      json=body,
                                      expected_status_code=200
                                      )

        self.status = response.status_code
        self.response = response.json()
        return response

    def check_booking_in_response_body(self):
        assert "booking" in self.response, "Тело ответа не содержит объект 'booking'"
        self.bookings = self.response["booking"]

    def check_lastname(self, expected_lastname):
        assert self.bookings["lastname"] == expected_lastname

    def check_additionalneeds(self, additionalneeds):
        assert self.bookings["additionalneeds"] == additionalneeds

        print(self.response)
