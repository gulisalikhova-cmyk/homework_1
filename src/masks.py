def get_mask_card_number(card_number: str) -> str:
    """Функция получает номер карты пользователя и возвращает замаскированный номер"""

    card_number = card_number.replace(" ", "")
    try:
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Номер карты должен содержать 16 цифр")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    except ValueError as e:
        return f"Ошибка: {e}"


bank_card_number = input()
print(get_mask_card_number(bank_card_number))


def get_mask_account(account: str) -> str:
    """Функция принимает номер счета и выводит его маску"""

    account = account.replace(" ", "")
    try:
        if len(account) != 20 or not account.isdigit():
            raise ValueError("Номер счета должен содержать 20 цифр")
        return f"**{account[-4:]}"

    except ValueError as e:
        return f"Ошибка: {e}"


user_account = input()
print(get_mask_account(user_account))
