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
