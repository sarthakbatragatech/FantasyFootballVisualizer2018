import pandas as pd 
import boto3
from decimal import Decimal

def addData():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('FFPoints')

    data = pd.read_csv("pointsAgainst.csv")

    print(data.head())

    teams = data['Team']
    abbrs = data['Abbr']
    points = data['AvgPtsAllowed']

    print(points.mean())

    print("\n")
    print(table.creation_date_time)
    print("\n")

# Check the right way to put data, perhaps range affecting order, NE first

    with table.batch_writer() as batch:
        for i in range(32):
            batch.put_item(
                Item={
                    'Team': abbrs[i],
                    'Week 10': str(points[i])
                }
            )

addData()