import json
import boto3
from botocore.exceptions import ClientError
from events.convert_json import convert_to_json

def get(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('godswork-api-dev-events')

    # Retrieve all items from DynamoDB
    try:
        response = table.scan()
        items = response['Items']

        # Convert DynamoDB items to the desired structure
        formatted_items = []
        for item in items:
            formatted_items.append(convert_to_json(item))

        print(formatted_items)

        # Use json.dumps to convert the list of items to a JSON string
        json_response = json.dumps(formatted_items)

        return {
            'statusCode': 200,
            'body': json_response
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
