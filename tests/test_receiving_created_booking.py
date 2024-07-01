from endpoints.receiving_create_booking import ReceiveBooking
import pytest


@pytest.mark.booking
def test_getting_book(send_book_id):
    endpoint = ReceiveBooking()
    endpoint.get_create_booking(send_book_id)
    endpoint.check_request_status_code()
    endpoint.check_totalprice()
    endpoint.check_firstname()

