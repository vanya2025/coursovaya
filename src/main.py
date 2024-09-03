import json
from utils import mask_card_number, mask_account_number, format_date

def get_last_five_operations(file_path):
    try:
        with open(file_path, 'r') as file:
            operations = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading file: {e}")
        return []

    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)

    last_five_operations = sorted_operations[:5]

    result = []
    for op in last_five_operations:
        date = format_date(op['date'])
        description = op['description']
        from_account = op.get('from', '')
        to_account = op.get('to', '')
        amount = f"{op['operationAmount']['amount']} {op['operationAmount']['currency']['name']}"

        operation_info = f"{date} {description}\n"

        if from_account:
            if from_account.lower().startswith('счет'):
                from_account = f"Счет {mask_account_number(from_account)}"
            else:
                # Рассплитим карту и маскируем только номер
                card_parts = from_account.split()
                card_number = mask_card_number(card_parts[-1])
                from_account = ' '.join(card_parts[:-1]) + ' ' + card_number
            operation_info += f"{from_account} -> Счет {mask_account_number(to_account)}\n"
        else:
            operation_info += f"Счет {mask_account_number(to_account)}\n"

        operation_info += f"{amount}\n"
        result.append(operation_info)

    return result

if __name__ == "__main__":
    operations = get_last_five_operations('../data/operations.json')
    for operation in operations:
        print(operation)
