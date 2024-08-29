import allure
from endpoints.create_booking import Booking


@allure.title("Create bookings")
@allure.feature("Tests Booking")
@allure.story('Post')
def test_create_booking(generate_firstname, generate_lastname, generate_totalprice, generate_additionalneeds, checkin,
                        checkout):
    endpoint = Booking()
    endpoint._create_booking(generate_firstname, generate_lastname,
                             generate_totalprice, generate_additionalneeds, checkin, checkout
                             )
    endpoint.check_booking_in_response_body()
    endpoint.check_lastname(generate_lastname)
    endpoint.check_additionalneeds(generate_additionalneeds)



