import boto3

# ---- Creating First Table ----- 
create_table = {            # Optional line
    'TableName': 'Emloyees', # Table Name
    'KeySchema': [                                      # List of Attributes and KeyTypes
                    {                                   # First Attribute/Field/Column
                        'AttributeName' : 'Name',       # Field Name
                        'KeyType': 'HASH',              # primary key
                    }, 

                    {                                   # First Attribute/Field/Column
                        'AttributeName' : 'Email',      # Field Email
                        'KeyType': 'Range',             # secondary/sort key (optional) to create composite key with primary key
                    }, 
                ],        
        
        # Attribute Definitons: name(fieldName) and Types(string, int etc...)
        'AttributeDefinitions': [
        # Att. Type : 
        # 'S' : 'STRING', 
        # 'N' : 'NUMBER', 
        # 'BOOL' : 'BOOLEAN', 
        # 'B' : 'BINARY',
        # 'L' : 'LIST',
        # 'M' : 'MAP',
        # 'NULL' : 'NULL',
        # 'SS' : 'STRING SET', 
        # 'NS' : 'NUMBER SET', 
            
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'  # String type
        },

        {
            'AttributeName': 'Email',
            'AttributeType': 'S'  # String type
        }
    ],

    # Read and Write per second 
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    }
}


# Create a DynamoDB client using boto3
client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

# Create the above table
response = client.create_table(**create_table) # unpack the above table 

# Another way to create the above table
# response = client.create_table(TableName = table_name, KeySchema = key_schema, AttributeDefinition = attribute_definitions, ProvisionedThroughput = provisioned_throughput)

# Wait for the table to be created
waiter = client.get_waiter('table_exists')
waiter.wait(TableName='Employees')

print(f"Table '{response['TableDescription']['TableName']}' created successfully.")
print(response)