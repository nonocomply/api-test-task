from typing import Type

import allure
from pydantic import BaseModel, ValidationError
from requests import Response


def assert_schema(response, model: Type[BaseModel]):
    """
    Проверяет тело ответа на соответствие его модели pydantic

    :param response: Ответ от сервера
    :param model: Модель, по которой будет проверяться схема json
    :raises ValidationError: Если тело ответа не соответствует схеме
    """
    body = response.json()
    try:
        if isinstance(body, list):
            for index, item in enumerate(body):
                try:
                    model.model_validate(item, strict=False)
                except ValidationError as e:
                    allure.attach(
                        str(e),
                        name=f"Ошибка валидации для элемента [{index}]",
                        attachment_type=allure.attachment_type.TEXT,
                    )
                    raise AssertionError(
                        f"Pydantic: ошибка валидации элемента с индексом [{index}]"
                    ) from e
        else:
            model.model_validate(body, strict=False)

    except ValidationError as e:
        allure.attach(
            str(e),
            name="Ошибка валидации ответа",
            attachment_type=allure.attachment_type.TEXT,
        )
        raise AssertionError("Pydantic: тело ответа не соответствует схеме") from e


def assert_status_code(response: Response, expected_code):
    """
    Сравнивает код ответа от сервера с ожидаемым

    :param response: полученный от сервера ответ
    :param expected_code: ожидаемый код ответа
    :raises AssertionError: если значения не совпали
    """
    assert expected_code == response.status_code, (
        f"Ожидался {expected_code} статус-код, но в ответе {response.status_code}",
        f"{response.url}",
        f"{response.json()}",
    )


def assert_field_required(response: Response):
    """
    Проверяет, что в ответе содержится сообщение об обязательном поле.

    :param response: полученный от сервера ответ
    :raises AssertionError: если сообщение об обязательном поле отсутствует или не совпадает
    """
    expected_message = "Не передан обязательный параметр"
    error_message = response.json()["errors"][0]["message"]
    assert expected_message in error_message, (
        f"Ожидалось сообщение об ошибке содержит: '{expected_message}', "
        f"но получено: '{error_message}'"
    )


def assert_not_found(response: Response):
    """
    Проверяет, что в ответе содержится сообщение об отсутсвтии ресурса.

    :param response: полученный от сервера ответ
    :raises AssertionError: если сообщение о об обтсутствие отсутствует или не совпадает
    """
    expected_message = "не найден"
    error_message = response.json()["message"]
    assert expected_message in error_message, (
        f"Ожидалось сообщение об ошибке содержит: '{expected_message}', "
        f"но получено: '{error_message}'"
    )


if __name__ == "__main__":
    pass
