from endpoints.receive_token_authorization import ReceiveToken
import pytest


@pytest.mark.booking
def test_authorization():
    endpoint = ReceiveToken()
    endpoint.send_request_for_authorization()
    endpoint.check_response_status_is_ok()
    endpoint.check_token_in_response()





