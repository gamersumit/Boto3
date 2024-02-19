# put / insert

import boto3

# Create a DynamoDB client using boto3
client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

# define table name where you want to insert data
table_name = 'Emloyees'

# define item to insert
item = {
 'Name': {'S' : 'Emp1'},
 'Email': {'S': 'emp1@gmali.com'},   
}

# insert item into table
response = client.put_item(
    TableName = table_name,
    Item = item
)


print(response)