import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ItemTable')


def lambda_handler(event, context):
    try:

        item_id = str(event['id'])

        # Check for valid path parameter
        if not item_id.isnumeric():
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid request format. Id must be a valid number.'})
            }

        item_id = int(item_id)

        response = table.get_item(
            Key={
                'id': item_id
            }
        )

        # Check if the given id is in the table
        if 'Item' in response:
            item = response['Item']
            item['id'] = int(item['id'])
            return {
                'statusCode': 200,
                'body': json.dumps(item)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Item not found.'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
