from clients.http_client import HTTPClient


class ReceiveBooking(HTTPClient):

    def __init__(self):
        self._http_client_ = HTTPClient()

    def get_create_booking(self, book_id):
        response = self._send_request(url=f"https://restful-booker.herokuapp.com/booking/{book_id}",
                                      method="get",
                                      expected_status_code=200
                                      )
        self.status = response.status_code
        self.response = response.json()
        return self.response

    def check_firstname(self):
        assert len(self.response["firstname"]) > 0

    def check_totalprice(self):
        assert self.response["totalprice"] > 0

        print(self.response)

