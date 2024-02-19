import boto3

# Create a DynamoDB client using boto3
client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

tables = client.list_tables()

print("Table Var/RESPONSE/OBJ: ", tables)       # all the tables names and Response Metadata
print("table response type: ", type(tables))    # dictionary
# print("TableNames: ", tables['tableNames'])