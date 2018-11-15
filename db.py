import boto3

# Get the service resource
dynamodb = boto3.resource('dynamodb')

 # Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='FFPoints',
    KeySchema=[
        {
            'AttributeName': 'Team',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Team',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='FFPoints')

print(table.item_count)