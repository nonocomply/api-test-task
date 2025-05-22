import allure
import requests
from requests import Response


class BaseAPI:
    def __init__(self, token: str = None):
        self.default_headers = {}
        if token:
            self.default_headers["Authorization"] = f"Bearer {token}"

    @allure.step("GET-запрос: {path}")
    def get(self, path: str, params=None, headers: dict = None) -> Response:
        url = path
        headers = {**self.default_headers, **(headers or {})}
        response = requests.get(url, params=params, headers=headers)

        return response


if __name__ == "__main__":
    pass
