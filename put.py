import json
import boto3
from decimal import Decimal

# Initialize DynamoDB resource and table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GroceryItems')

def lambda_handler(event, context):
    # Log the event to check its structure
    print("Event:", json.dumps(event))

    # Ensure 'body' exists in the event
    if 'body' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing body in the request'})
        }

    try:
        # Parse the body and log it
        data = json.loads(event['body'])
        print("Parsed body:", json.dumps(data))  # Log the parsed body for debugging

        # Ensure 'pathParameters' exists and contains 'itemid'
        if 'pathParameters' not in event or 'itemid' not in event['pathParameters']:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': "Missing 'itemid' in path parameters"})
            }

        # Retrieve the item ID from path parameters
        item_id = event['pathParameters']['itemid']

        # Extract and validate fields from the body
        if 'name' not in data or 'price' not in data or 'category' not in data:
            missing_fields = [field for field in ['name', 'price', 'category'] if field not in data]
            return {
                'statusCode': 400,
                'body': json.dumps({'error': f"Missing field(s): {', '.join(missing_fields)}"})
            }

        # Convert price to Decimal
        price = Decimal(str(data['price']))

        # Update expression to avoid reserved words
        update_expression = "SET #name = :name, Price = :price, Category = :category"
        expression_values = {
            ':name': data['name'],
            ':price': price,
            ':category': data['category']
        }
        expression_attribute_names = {
            '#name': 'Name'  # Alias 'Name' as '#name'
        }

        # Update the item in DynamoDB
        table.update_item(
            Key={'ItemID': item_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values,
            ExpressionAttributeNames=expression_attribute_names
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item updated successfully'})
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': "Invalid JSON"})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
