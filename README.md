# Тестовое задание

Этот проект содержит автотесты для проверки API, выполненные в рамках тестового задания.

## Стек

- Python 3.12
- [pytest](https://docs.pytest.org/)
- [requests](https://docs.python-requests.org/)
- [allure-pytest](https://github.com/allure-framework/allure-python)
- [pydantic](https://docs.pydantic.dev/)

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/bnovo-api-tests.git
cd bnovo-api-tests
```
2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate # Для macOS/Linux
venv\Scripts\activate # Для Windows
```
3. Установите зависимости

```bash
pip install -r requirements.txt
```

4. Создайте .env файл в корне проекта
```dotenv
BASE_URL=https://example.ru/v1/api # Пример URL
```

## Запуск тестов
Запустить все тесты
```bash
pytest
```

Запустить тесты с сохраненем результатов для Allure:
```bash
pytest --alluredir=allure-results
```

## Просмотр отчета Allure

Сгенерируйте HTML-отчет
```bash
allure generate allure-results --clean
```

Откройте отчет в браузере
```bash
allure open allure-report
```

Или сразу открыть с помощью serve
```bash
allure serve
```
