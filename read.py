
import boto3

# Create a DynamoDB client using boto3
client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

# define table name where you want to insert data
table_name = 'Emloyees'

# both partion and sort keys are required to read if a table has both
key = {
    'Name': {'S' : 'Emp1'},
    'Email': {'S': 'emp1@gmali.com'}, 
}

# Read the item from the table
response = client.get_item(
    TableName=table_name,
    Key=key
)


if 'Item' in response:
    item = response['Item']
    # Process the item
    print("Item:", item)
else:
    print("Item not found.")