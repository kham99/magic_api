import allure
from endpoints.receive_token_authorization import ReceiveToken


@allure.title("Receive token")
@allure.feature("Tests Booking")
@allure.story('Post')
def test_authorization():
    endpoint = ReceiveToken()
    endpoint._authorization()
    endpoint.check_token_in_response()
