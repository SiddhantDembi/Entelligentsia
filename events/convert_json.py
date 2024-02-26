from decimal import Decimal
import uuid

def convert_to_json(item):
    json_item = {}
    for key, value in item.items():
        if isinstance(value, Decimal):
            json_item[key] = str(value)
        elif isinstance(value, uuid.UUID):
            json_item[key] = str(value)
        elif isinstance(value, dict):
            json_item[key] = convert_to_json(value)
        else:
            json_item[key] = value
    return json_item