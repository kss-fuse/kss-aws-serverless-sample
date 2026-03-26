import json

def lambda_handler(event, context):

    auth_header = event.get("headers", {}).get("authorization")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "JWT received",
            "authorization": auth_header
        })
    }