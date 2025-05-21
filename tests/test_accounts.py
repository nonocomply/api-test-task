import allure
import pytest

from api.hotels.hotels_api import HotelsAPI
from api.hotels.models.account_model import AccountModel
from assertions.assertions import (
    assert_status_code,
    assert_schema,
    assert_field_required,
    assert_not_found,
)


@allure.feature("Получение мета-информации об отеле")
class TestAccounts:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api = HotelsAPI()

    @allure.story("Получение мета-информации об отеле по корректному UID")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_account_valid_uid(self):
        with allure.step("Отправить запрос на получение мета-информации об отеле"):
            response = self.api.get_account_meta_info(
                uid="d7494710-8c8c-4c4c-bba4-f71caf96fece"
            )
        with allure.step("Проверка статус кода ответа"):
            assert_status_code(response, 200)
        with allure.step("Валидация полей модели ответа"):
            assert_schema(response, AccountModel)

    @allure.story("Получение мета-информации об отеле без UID")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_account_without_uid(self):
        with allure.step("Отправить запрос на получение мета-информации об отеле"):
            response = self.api.get_account_meta_info(uid="")
        with allure.step("Проверка статус кода ответа"):
            assert_status_code(response, 406)
        with allure.step("Проверка сообщения об ошибки"):
            assert_field_required(response)

    @pytest.mark.parametrize(
        "invalid_uid",
        [
            20,
            "string",
            "ffffffff-ffff-ffff-ffff-ffffffffffff",
        ],
    )
    @allure.story("Получение мета-информации об отеле с невалидным UID")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_account_invalid_uid(self, invalid_uid):
        with allure.step("Отправить запрос на получение мета-информации об отеле"):
            response = self.api.get_account_meta_info(uid=invalid_uid)
        with allure.step("Проверка статус кода ответа"):
            assert_status_code(response, 404)
        with allure.step("Проверка сообщения об ошибки"):
            assert_not_found(response)
