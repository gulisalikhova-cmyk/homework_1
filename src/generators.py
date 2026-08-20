def filter_by_currency(transactions, currency_code):
    """Фильтрует транзакции по валюте."""
    for transaction in transactions:
        if "operationAmount" in transaction and "currency" in transaction["operationAmount"]:
            if transaction["operationAmount"]["currency"].get("code") == currency_code:
                yield transaction
