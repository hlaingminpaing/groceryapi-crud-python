import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GroceryItems')

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))  # Log the received event for debugging
    try:
        # Ensure the body is parsed from the event
        body = json.loads(event['body'])
        print("Parsed body:", json.dumps(body))  # Log the parsed body for debugging

        # Extract fields from the parsed body
        name = body.get('name')
        price = body.get('price')
        category = body.get('category')
        item_id = body.get('itemid')

        # Check for missing fields
        if not all([name, price, category, item_id]):
            missing_fields = [field for field in ['name', 'price', 'category', 'itemid'] if not body.get(field)]
            return {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST"
                },
                "body": json.dumps({"error": f"Missing field(s): {', '.join(missing_fields)}"})
            }
        
        # Convert price to Decimal
        price = Decimal(str(price))
        
        # Save the item in DynamoDB
        table.put_item(
            Item={
                'ItemID': item_id,
                'Name': name,
                'Price': price,
                'Category': category
            }
        )
        
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({"message": "Item added successfully!"})
        }
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({"error": "Invalid JSON"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({"error": str(e)})
        }
