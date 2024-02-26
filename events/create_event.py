import os
import uuid
import boto3
import json
from decimal import Decimal
from boto3.dynamodb.conditions import Attr

from validators import validate_events

dynamodb = boto3.resource("dynamodb")


def create(event, context):
    if "body" not in event:
        return {"statusCode": 400, "body": "Invalid input. Missing body."}

    if event["body"] is None:
        return {"statusCode": 400, "body": "Invalid input. Missing body."}

    created_event = json.loads(event["body"])

    if not validate_events(created_event):
        return {"statusCode": 400, "body": "Invalid body."}

    found_user = dynamodb.Table(os.environ["USER_TABLE"]).scan(
        FilterExpression=Attr("id").eq(
            event["requestContext"]["authorizer"]["principalId"]
        )
    )

    organizer = found_user["Items"][0]

    created_event["id"] = str(uuid.uuid1())
    created_event["attendees"] = [organizer["id"]]
    created_event["organiser"] = organizer["id"]
    created_event["creater"] = organizer["id"]
    created_event["requiredParticipants"] = (
        created_event["requiredParticipants"]
        if "requiredParticipants" in created_event
        else 0
    )

    events = dynamodb.Table(os.environ["EVENTS_TABLE"])

    events.put_item(Item=json.loads(json.dumps(created_event), parse_float=Decimal))

    response = {
        "statusCode": 200,
        "body": json.dumps(created_event),
    }

    return response
