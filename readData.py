import boto3
from boto3.dynamodb.conditions import Key, Attr


def readData():
    teams = []
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('FFPoints')

    # item = table.get_item(Key={'Team': 'NE'})['Item']['Week 10']
    # print(item)
    # assert float(item) == 18.54

    response = table.scan()
    data = response['Items']
    
    # values = []
    # for dict_item in data:
        # for key, value in dict_item.items():
            # values.append(value)
    # return(values)
    return(data)

a = readData()
