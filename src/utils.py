from datetime import datetime

def mask_card_number(card_number):
    """Маскирует номер карты, скрывая середину."""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def mask_account_number(account_number):
    """Маскирует номер счета, скрывая первые символы."""
    return f"**{account_number[-4:]}"

def format_date(date_str):
    """Форматирует дату в формате DD.MM.YYYY."""
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
