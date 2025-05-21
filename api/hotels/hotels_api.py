import pprint
from typing import Union

from requests import Response

from api.base_api import BaseAPI
from api.hotels.endpoints import Endpoints


class HotelsAPI(BaseAPI):
    def __init__(self):
        self.endpoints = Endpoints()

    def get_account_meta_info(self, uid: str) -> Response:
        """
        Метод для получения мета-информации об отеле

        :param uid: UID модуля бронирования отеля
        :return requests.Response:
        """
        params = {}

        if uid is not None:
            params["uid"] = uid

        return self.get(path=self.endpoints.get_accounts, params=params)

    def get_roomtypes(
        self,
        account_id: Union[str, int, None],
        address_included: Union[str, int],
        headers: dict = None,
    ) -> Response:
        """
        Метод для получения данных о категориях номеров

        :param headers: Хедеры запроса
        :param account_id: Идентификатор аккаунта
        :param address_included: Показать данные местоположения. 0 - не показывать, 1 - показывать.
        :return requests.Response:
        """
        params = {}

        if account_id is not None:
            params["account_id"] = account_id
        if address_included is not None:
            params["address_included"] = address_included

        return self.get(
            path=self.endpoints.get_roomtypes,
            params=params,
            headers=headers,
        )

    def get_plans(self, account_id: int = None) -> Response:
        """
        Метод для получения данных о тарифах

        :param account_id: Идентификатор аккаунта
        :return requests.Response:
        """
        params = {}

        if account_id is not None:
            params["account_id"] = account_id

        return self.get(path=self.endpoints.get_plans, params=params)


if __name__ == "__main__":
    api = HotelsAPI()
    response = api.get_meta_info(uid="d7494710-8c8c-4c4c-bba4-f71caf96fece")
    pprint.pprint(response.json())
