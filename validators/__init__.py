import re


def validate_input(field_name, input_value):
    regex_patterns = {
        "mobile_number": r"^(\+\d{1,3}[- ]?)?\d{10}$",
        "whatsapp_number": r"^(\+\d{1,3}[- ]?)?\d{10}$",
        "username": r"^[A-Za-z]\w{5,29}$",
        "full_name": r"^[a-zA-Z]+ [a-zA-Z]+$",
        "password": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
    }

    if field_name in regex_patterns:
        regex_pattern = regex_patterns[field_name]
        if not re.match(regex_pattern, input_value):
            print(f"Error: {field_name} does not match the expected pattern.")
            return False

    elif field_name == "address":
        if not validate_address(input_value):
            return False

    else:
        print(f"Error: Invalid field name '{field_name}'.")
        return False

    return True


def validate_address(address):
    try:
        if not address["cityOrVillage"].isalpha():
            raise ValueError("Error: City or village must contain only alphabets.")
        if not address["state"].isalpha():
            raise ValueError("Error: State must contain only alphabets.")
        if not address["country"].isalpha():
            raise ValueError("Error: Country must contain only alphabets.")

        float(address["latitude"])
        float(address["longitude"])
    except KeyError as e:
        print(f"Error: {e} is missing in the address.")
        return False
    except (ValueError, TypeError):
        print("Error: Invalid value or type in the address.")
        return False

    return True


def validate_participant(participant):
    try:
        if not participant["name"].isalpha():
            raise ValueError("Error: Name must contain only alphabets.")

        if not validate_input("mobile_number", participant["mobileNumber"]):
            return False

        if not validate_input("whatsapp_number", participant["whatsappNumber"]):
            return False

    except KeyError as e:
        print(f"Error: {e} is missing in the participant.")
        return False
    except ValueError as e:
        print(e)
        return False

    return True


def validate_events(event):
    regex_patterns = {
        "id": r"^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$",
        "eventId": r"^[0-9]{4}-[0-9]{4}$",
        "eventType": r"^[a-zA-Z0-9, ]+$",
        "dateandtime": r"^20[0-9]{2}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\+[0-9]{4}$",
        "participant_amount": r"^[0-9]+$",
        "required_participants": r"^[0-9]+$",
        "total_amount": r"^[0-9]+$",
        "participant_amount": r"^[0-9]+$",
    }

    for field_name, input_value in event.items():
        if field_name in regex_patterns:
            regex_pattern = regex_patterns[field_name]
            if not re.match(regex_pattern, str(input_value)):
                print(f"Error: {field_name} does not match the expected pattern.")
                return False

        elif field_name == "address":
            if not validate_address(input_value):
                return False

        elif field_name in ["attendees", "organiser", "creater"]:
            if not validate_participant(input_value):
                return False

        else:
            print(f"Error: Invalid field name '{field_name}'.")
            return False

    return True
