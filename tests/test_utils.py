import pytest
from src.utils import mask_card_number, mask_account_number, format_date

def test_mask_card_number():
    assert mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert mask_card_number("6543210987654321") == "6543 21** **** 4321"

def test_mask_account_number():
    assert mask_account_number("12345678") == "**5678"
    assert mask_account_number("87654321") == "**4321"

def test_format_date():
    assert format_date("2022-01-01T12:00:00.000") == "01.01.2022"
    assert format_date("2023-12-31T23:59:59.999") == "31.12.2023"
