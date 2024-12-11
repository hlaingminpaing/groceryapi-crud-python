import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GroceryItems')

def lambda_handler(event, context):
    item_id = event['pathParameters']['id']
    
    try:
        # Try to delete the item
        response = table.delete_item(
            Key={'ItemID': item_id},
            ReturnValues='ALL_OLD'  # Return the deleted item
        )
        
        # Check if the item was found and deleted
        if 'Attributes' in response:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Item deleted successfully'})
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Item not found'})
            }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
