import json

def lambda_handler(event, context):

    headers = event.get("headers", {})
    auth = headers.get("Authorization") or headers.get("authorization")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "JWT received",
            "authorization": auth
        })
    }