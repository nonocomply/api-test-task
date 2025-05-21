from requests import Response


def assert_field_is_not_empty(response: Response, field):
    """
    Проверяет, что поле с заданным именем не пустое.

    :param response: requests.Response
    :param field: Название поля (например, "name_ru")
    :raises AssertionError: Если поле отсутствует или все его значения пустые
    """
    data = response.json()["rooms"]
    items = data if isinstance(data, list) else [data]
    values = []

    for item in items:
        if isinstance(item, dict) and field in item:
            values.append(item.get(field))

    assert values, f"Поле '{field}' не найдено ни в одном элементе"
    assert any(
        v not in (None, "", [], {}) for v in values
    ), f"Поле '{field}' найдено, но все значения пустые"


if __name__ == "__main__":
    pass
