import allure
from endpoints.receiving_create_booking import ReceiveBooking


@allure.title("Receiving create booking")
@allure.feature("Tests Booking")
@allure.story('Get')
def test_getting_book(send_book_id):
    endpoint = ReceiveBooking()
    endpoint.get_create_booking(send_book_id)
    endpoint.check_totalprice()
    endpoint.check_firstname()

