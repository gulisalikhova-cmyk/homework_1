import pytest
from src.masks import get_mask_card_number, get_mask_account
from tests.conftest import card_number, account_number


def test_card_normal(card_number):
    """Тестирует правильность маскировки номера карты."""
    result = get_mask_card_number(card_number)
    assert result == "1234 56** **** 3456"

def test_card_with_spaces():
    """Тестирует маскировку номера карты с пробелами."""
    result = get_mask_card_number("1234 5678 9012 3456")
    assert result == "1234 56** **** 3456"

def test_card_short():
    """Тестирует обработку короткого номера карты (<16 цифр)."""
    result = get_mask_card_number("1234567890")
    assert "Ошибка" in result

def test_card_empty():
    """Тестирует обработку пустой строки для номера карты."""
    result = get_mask_card_number("")
    assert "Ошибка" in result

def test_account_normal(account_number):
    """Тестирует правильность маскировки номера счета."""
    result = get_mask_account(account_number)
    assert result == "**7890"

def test_account_short():
    """Тестирует обработку короткого номера счета (<20 цифр)"""
    result = get_mask_account("1234567890")
    assert "Ошибка" in result

def test_account_empty():
    """Тестирует обработку пустой строки для номера счета."""
    result = get_mask_account("")
    assert "Ошибка" in result
