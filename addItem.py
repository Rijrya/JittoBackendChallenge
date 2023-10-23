import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ItemTable')
counter_table = dynamodb.Table('TableCounter')


def lambda_handler(event, context):
    try:
        name = event['name']
        description = event['description']

    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request format.'})
        }

    # Check if both parameters were given
    if not name or not description:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Missing required fields in the request.'})
        }

    # Generate a new id for the item
    item_id = int(generate_new_id())

    # format the item data
    item_data = {
        "id": item_id,
        "name": name,
        "description": description
    }

    table.put_item(Item=item_data)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item added successfully', 'item_id': item_id})
    }


# Function to update the last_id attribute in the counter table, and return the updated value.
def generate_new_id():
    response = counter_table.update_item(
        Key={'counter_name': 'item_counter'},
        UpdateExpression='SET last_id = last_id + :increment',
        ExpressionAttributeValues={':increment': 1},
        ReturnValues='UPDATED_NEW'
    )
    return response['Attributes']['last_id']