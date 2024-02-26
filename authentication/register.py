import json
import os
import time
import uuid
from validators import validate_input
import hashlib
import boto3

dynamodb = boto3.resource("dynamodb")


def register(event, context):
    if "body" not in event:
        print("Validation Failed")
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid input."})}

    data = json.loads(event["body"])

    if not validate_input("username", data["username"]):
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid username."})}
    if not validate_input("password", data["password"]):
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid password."})}
    if not validate_input("whatsapp_number", data["whatsappNumber"]):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid whatsapp number."}),
        }
    if not validate_input("mobile_number", data["mobileNumber"]):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid mobile number."}),
        }
    if not validate_input("full_name", data["name"]):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid full name."}),
        }
    if not validate_input("address", data["address"]):
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid address."})}

    table = dynamodb.Table(os.environ["USER_TABLE"])
    timestamp = str(time.time())

    item = {
        "id": str(uuid.uuid1()),
        "username": data["username"],
        "hash": hashlib.sha256(
            (data["username"] + data["password"]).encode()
        ).hexdigest(),
        "mobileNumber": data["mobileNumber"],
        "whatsappNumber": data["whatsappNumber"],
        "fullName": data["name"],
        "address": json.dumps(data["address"]),
        "createdAt": timestamp,
        "updatedAt": timestamp,
    }

    table.put_item(Item=item)

    response = {"statusCode": 200, "body": json.dumps(item)}

    return response
