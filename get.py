import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GroceryItems')

# Function to convert Decimal to float
def decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, dict):
        return {key: decimal_to_float(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [decimal_to_float(item) for item in obj]
    return obj

def lambda_handler(event, context):
    # Perform scan operation to get items from DynamoDB table
    response = table.scan()
    items = response.get('Items', [])
    
    # Convert Decimal to float in the response items
    items = decimal_to_float(items)
    
    # Return the response with the body as a properly formatted JSON array
    return {
        'statusCode': 200,
        'body': items  # No json.dumps() here, return the actual list
    }
