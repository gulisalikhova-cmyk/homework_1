import pytest

@pytest.fixture
def card_number():
    """Возвращает правильный номер карты (16 цифр)."""
    return "1234567890123456"

@pytest.fixture
def account_number():
    """Возвращает правильный номер счета (20 цифр)."""
    return "12345678901234567890"

@pytest.fixture
def date_src():
    """Возвращает правильную дату в формате ISO."""
    return "2024-12-25"
