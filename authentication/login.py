import sys

sys.path.insert(0, "vendor")

import hashlib
import json
import os
import boto3
import jwt
from boto3.dynamodb.conditions import Attr

from validators import validate_input


dynamodb = boto3.resource("dynamodb")


def login(event, context):
    if "body" not in event:
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid input."})}
    if event["body"] is None:
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid input."})}
    
    data = json.loads(event["body"])

    if not validate_input("username", data["username"]):
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid username."})}
    if not validate_input("password", data["password"]):
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid password."})}

    table = dynamodb.Table(os.environ["USER_TABLE"])

    response = table.scan(FilterExpression=Attr("username").eq(data["username"]))

    if "Items" not in response:
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid username."})}

    user = response["Items"]

    if len(user) == 0:
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid username."})}

    user = user[0]

    if (
        user["hash"]
        != hashlib.sha256((data["username"] + data["password"]).encode()).hexdigest()
    ):
        return {"statusCode": 400, "body": json.dumps({"message": "Invalid password."})}

    secret = (
        boto3.Session(
            aws_access_key_id=os.environ["AWS_ID"],
            aws_secret_access_key=os.environ["AWS_KEY"],
        )
        .client(service_name="secretsmanager", region_name="ap-south-1")
        .get_secret_value(SecretId="JWT_KEY")
    )
    if "SecretString" in secret:
        jwt_key = secret["SecretString"]
    else:
        jwt_key = secret["SecretBinary"]

    token = jwt.encode(user, jwt_key, algorithm="HS512")

    return {"statusCode": 200, "body": json.dumps({"token": token})}
