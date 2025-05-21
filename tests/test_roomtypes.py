from pprint import pprint

import allure
import pytest

from api.hotels.hotels_api import HotelsAPI
from api.hotels.models.roomtypes_model import RoomsModel
from assertions.assertions import (
    assert_schema,
    assert_status_code,
    assert_field_required,
    assert_not_found,
)
from assertions.roomtypes_assertions import assert_field_is_not_empty


@allure.feature("Получение данных о категориях номеров")
class TestRoomTypes:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api = HotelsAPI()

    @pytest.mark.parametrize(
        "account_id, address_included",
        [
            (535, 1),
            (535, 0),
            (535, None),
        ],
        ids=[
            "valid account_id, address_included on",
            "valid account_id, address_included off",
            "valid account_id without address_included",
        ],
    )
    @allure.story("Получение данных о категориях номеров с валидными параметрами")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_room_types(self, account_id, address_included):
        with allure.step("Отправить запрос на получение данных о категориях номеров"):
            response = self.api.get_roomtypes(
                account_id=account_id, address_included=address_included
            )
        with allure.step("Проверка статус кода ответа"):
            assert_status_code(response, 200)
        with allure.step("Валидация полей модели ответа"):
            assert_schema(response, RoomsModel)

    @allure.story("Получение данных о категориях номеров без account_id")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_room_types_without_account_id(self):
        with allure.step("Отправить запрос на получение данных о категориях номеров"):
            response = self.api.get_roomtypes(account_id=None, address_included=1)
        with allure.step("Проверка статус кода ответа"):
            assert_status_code(response, 406)
        with allure.step("Проверка сообщения об ошибки"):
            assert_field_required(response)

    @allure.story("Получение данных о категориях номеров c несущствующим account_id")
    def test_get_room_types_not_found(self):
        with allure.step("Отправить запрос на получение данных о категориях номеров"):
            response = self.api.get_roomtypes(account_id=99999999, address_included=0)
        with allure.step("Проверка статус кода ответа"):
            assert_status_code(response, 404)
        with allure.step("Проверка сообщения об ошибки"):
            assert_not_found(response)

    @pytest.mark.parametrize(
        "account_id, address_included",
        [("string", 1), (535, 2), (535, "string"), (535, -1)],
        ids=[
            "Invalid data type account_id",
            "Not valid address_included",
            "Invalid data type address_included",
            "Negative int address_included",
        ],
    )
    @allure.story("Получение данных о категориях номеров c невалидными параметрами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_room_types_invalid_params(self, account_id, address_included):
        with allure.step("Отправить запрос на получение данных о категориях номеров"):
            response = self.api.get_roomtypes(
                account_id=account_id, address_included=address_included
            )
        with allure.step("Проверка статус кода ответа"):
            assert_status_code(response, 400)
        with allure.step("Проверка сообщения об ошибки"):
            assert_not_found(response)

    @pytest.mark.parametrize(
        "lang, expected_field",
        [
            ("ru", "name_ru"),
            ("en", "name_en"),
            ("de", "name_de"),
            ("zh", "name_zh"),
            ("es", "name_es"),
            ("fr", "name_fr"),
            ("ja", "name_ja"),
            ("it", "name_it"),
            ("ko", "name_ko"),
            ("pl", "name_pl"),
            ("fi", "name_fi"),
            ("lt", "name_lt"),
            ("ro", "name_ro"),
            ("lv", "name_lv"),
            ("uk", "name_uk"),
            ("hy", "name_hy"),
        ],
        ids=[
            f"Locale test for lang={lang}"
            for lang in [
                "ru",
                "en",
                "de",
                "zh",
                "es",
                "fr",
                "ja",
                "it",
                "ko",
                "pl",
                "fi",
                "lt",
                "ro",
                "lv",
                "uk",
                "hy",
            ]
        ],
    )
    @allure.story("Локализация категорий по Accept-Language")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_localization_room_types(self, lang, expected_field):
        headers = {"Accept-Language": lang}
        with allure.step("Отправить запрос на получение данных о категориях номеров"):
            response = self.api.get_roomtypes(
                account_id=535, address_included=1, headers=headers
            )
        with allure.step("Проверка статус кода"):
            assert_status_code(response, 200)
        with allure.step(f"Проверка, что поле '{expected_field}' не пустое"):
            assert_field_is_not_empty(response, expected_field)


if __name__ == "__main__":
    pass
