from endpoints.create_booking import CreateBooking
import pytest


@pytest.mark.booking
def test_create_booking(generate_firstname, generate_lastname, generate_totalprice, generate_additionalneeds):
    endpoint = CreateBooking()
    endpoint.send_request_for_create_booking(generate_firstname, generate_lastname,
                                             generate_totalprice, generate_additionalneeds)
    endpoint.check_request_status_code()
    endpoint.check_booking_in_response_body()
    endpoint.check_lastname(generate_lastname)
    endpoint.check_additionalneeds(generate_additionalneeds)



