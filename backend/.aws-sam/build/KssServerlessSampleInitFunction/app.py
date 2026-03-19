import json

def lambda_handler(event, context):

    body = {
        "message": "Hello from Lambda"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }