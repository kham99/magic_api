from typing import Optional
import requests


class HTTPClient:
    def get(self, url, expected_status_code: Optional[int] = None, params: Optional[dict] = None):
        response = self._send_request(url=url, method="get", params=params, expected_status_code=expected_status_code)
        return response

    def _send_request(self, url: str, method: str, expected_status_code: Optional[int] = None, **kwargs):
        response = requests.request(method=method, url=url, **kwargs)
        if expected_status_code:
            assert response.status_code == expected_status_code, (f"Expected status code {expected_status_code}, "
                                                                  f"got {response.status_code}")
        return response

