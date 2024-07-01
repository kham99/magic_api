from endpoints.receiving_create_booking import ReceiveBooking


def test_getting_book():
    endpoint = ReceiveBooking()
    endpoint.get_create_booking()
    endpoint.check_request_status_code()

