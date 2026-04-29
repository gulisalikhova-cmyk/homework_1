from datetime import datetime


def mask_account_card(account_card: str) -> str:
    """Функция обрабатывает информацию о картах и о счетах. Возвращает тип и замаскированный номер"""
    try:
        if not account_card or account_card.strip() == "":
            raise ValueError("Пустая строка")

        list_info = account_card.split(" ")

        if len(list_info) != 2 or not list_info[1].isdigit():
            raise ValueError("Нужно вести тип и номер карты или счета")
        if len(list_info[1]) == 16:
            return f"{list_info[0]} {list_info[1][:4]} {list_info[1][4:6]}** **** {list_info[1][-4:]}"
        elif len(list_info[1]) == 20:
            return f"{list_info[0]} **{list_info[1][-4:]}"
        else:
            raise ValueError(f"Длина номера {len(list_info[1])}. Нужно 16, либо 20")

    except ValueError as e:
        return f"Ошибка: {e}"


user_account_card = input()
print(mask_account_card(user_account_card))


def get_date(date_now: str) -> str:
    """Функция принимает на вход строку с датой в одном формате и возвращает строку в другом формате"""
    date_format = datetime.fromisoformat(date_now)
    return date_format.strftime("%d.%m.%Y")


datetime_now = input()
print(get_date(datetime_now))
