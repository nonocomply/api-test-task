from pprint import pprint

import allure
import pytest

from api.hotels.hotels_api import HotelsAPI
from api.hotels.models.plans_model import PlansModel
from assertions.assertions import (
    assert_status_code,
    assert_schema,
    assert_field_required,
    assert_not_found,
)


@allure.feature("Получение данных о тарифах")
class TestPlans:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api = HotelsAPI()

    @allure.story("Получение данных о тарифах с валидным account_id")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_plans(self):
        with allure.step("Отправить запрос на получение данных о тарифах"):
            response = self.api.get_plans(account_id=535)
        with allure.step("Проверка статус кода ответа"):
            assert_status_code(response, 200)
        with allure.step("Валидация полей модели ответа"):
            assert_schema(response, PlansModel)

    @allure.story("Получение данных о тарифах без account_id")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_plans_without_account_id(self):
        with allure.step("Отправить запрос на получение данных о тарифах"):
            response = self.api.get_plans()
        with allure.step("Проверка статус кода ответа"):
            assert_status_code(response, 406)
        with allure.step("Проверка сообщения об ошибки"):
            assert_field_required(response)

    @allure.story("Получение данных о тарифах с невалидным account_id")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_plans_invalid_account_id(self):
        with allure.step("Отправить запрос на получение данных о тарифах"):
            response = self.api.get_plans(account_id="string")
        with allure.step("Проверка статус кода ответа"):
            assert_status_code(response, 400)

    @allure.story("Получение данных о тарифах с невалидным account_id")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_plans_not_found(self):
        with allure.step("Отправить запрос на получение данных о тарифах"):
            response = self.api.get_plans(account_id=999999)
        with allure.step("Проверка статус кода ответа"):
            assert_status_code(response, 404)
        with allure.step("Проверка сообщения об ошибки"):
            assert_not_found(response)


if __name__ == "__main__":
    pass
