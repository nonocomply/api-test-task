from config.configuration import BASE_URL


class Endpoints:
    # Получение мета-информации об отеле
    get_accounts = f"{BASE_URL}/accounts"
    # Получение данных о категориях номеров
    get_roomtypes = f"{BASE_URL}/roomtypes"
    # Получение данных о тарифах
    get_plans = f"{BASE_URL}/plans"


if __name__ == "__main__":
    pass
