import pytest


@pytest.fixture
def transactions():
    return [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод USD"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Перевод EUR"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Оплата USD"},
    ]
