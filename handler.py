import json
import boto3
import os


from random import randint, choice
from datetime import datetime

course = (27, 28)

goods = ['book', 'bike', 'car']


# Get the service resource.
dynamodb = boto3.resource('dynamodb')


def check_stock_value(event, context):
    try:
        body = {
            "stock_price": randint(0, 100),
            "name": choice(goods),
            "datetime": datetime.now().strftime("%d-%m-%Y"),
        }
        table = dynamodb.Table(os.environ.get('DYNAMODB_NAME', 'stockTable'))
        table.put_item(Item=body)
    except Exception as e:
        print(f"Exception {str(e)}")
    print(body)
    return body


def sell(event, context):
    print(event)
    body = {
        "message": "Inside sell",
        "input": event,
        "stock_number": randint(0, 100)
    }
    print(body)
    return body


def buy(event, context):
    print(event)
    body = {
        "message": "Inside buy",
        "input": event,
        "stock_number": randint(0, 100)
    }
    print(body)
    return body
