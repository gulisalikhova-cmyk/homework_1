import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("data, currency, expected_count", [
    ([
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод USD"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Перевод EUR"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Оплата USD"},
    ], "USD", 2),   # Должно найти 2 транзакции с USD
    ([
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод USD"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Перевод EUR"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Оплата USD"},
    ], "EUR", 1),   # Должно найти 1 транзакцию с EUR
    ([
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод USD"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Перевод EUR"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Оплата USD"},
    ], "RUB", 0),   # Нет транзакций с RUB
])
def test_filter_by_currency(data, currency, expected_count):
    """Фильтрация по валюте с параметрами."""
    result = list(filter_by_currency(data, currency))
    assert len(result) == expected_count


@pytest.mark.parametrize("transactions, expected", [
    ([{"description": "A"}, {"description": "B"}], ["A", "B"]),
    ([{"description": "Test"}], ["Test"]),
    ([], []),
])
def test_transaction_descriptions(transactions, expected):
    """Получение описаний с параметрами."""
    result = list(transaction_descriptions(transactions))
    assert result == expected


@pytest.mark.parametrize("start, end, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (5, 5, ["0000 0000 0000 0005"]),
    (9999999999999990, 9999999999999992, [
        "9999 9999 9999 9990",
        "9999 9999 9999 9991",
        "9999 9999 9999 9992"
    ]),
])
def test_card_number_generator(start, end, expected):
    """Генерация номеров карт с параметрами."""
    result = list(card_number_generator(start, end))
    assert result == expected


def test_card_number_generator_format():
    """Проверка формата номера карты."""
    card = next(card_number_generator(1, 1))
    parts = card.split()
    assert len(parts) == 4
    assert all(len(p) == 4 and p.isdigit() for p in parts)
