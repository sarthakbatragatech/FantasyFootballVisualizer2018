import boto3
from boto3.dynamodb.conditions import Key, Attr


def readData():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('FFPoints')


    response = table.scan()
    items = response['Items']
    return items

a = readData()
for team in a:
    print(team)