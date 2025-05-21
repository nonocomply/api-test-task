import allure
import requests
from requests import Response


class BaseAPI:
    @allure.step("GET-запрос: {path}")
    def get(self, path: str, params=None, headers: dict = None) -> Response:
        url = path
        response = requests.get(url, params=params, headers=headers)

        return response


if __name__ == "__main__":
    pass
