def filter_by_currency(transactions, currency_code):
    """Фильтрует транзакции по валюте."""
    for transaction in transactions:
        if "operationAmount" in transaction and "currency" in transaction["operationAmount"]:
            if transaction["operationAmount"]["currency"].get("code") == currency_code:
                yield transaction


def transaction_descriptions(transactions):
    """Возвращает описания транзакций."""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start, end):
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        card_str = str(number).zfill(16)
        formatted = " ".join([card_str[i:i+4] for i in range(0, 16, 4)])
        yield formatted
