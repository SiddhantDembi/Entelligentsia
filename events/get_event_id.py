import json
import boto3
from botocore.exceptions import ClientError
from convert_json import convert_to_json

def get_event(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('godswork-api-dev-events')

    event_id = event['pathParameters']['id']

    try:
        response = table.get_item(Key={'id': event_id})
        item = response.get('Item')

        if item:
            formatted_item = convert_to_json(item)
            return {
                'statusCode': 200,
                'body': json.dumps(formatted_item)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Event not found'})
            }

    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
