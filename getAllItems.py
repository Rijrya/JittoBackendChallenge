import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ItemTable')


def lambda_handler(event, context):
    response = table.scan()
    items = response['Items']

    # Convert Decimal to int for the 'id' field
    for item in items:
        item['id'] = int(item['id'])

    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }
