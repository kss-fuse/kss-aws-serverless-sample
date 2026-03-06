from ..src.functions.init.app import lambda_handler

def test_lambda_handler():
    event = {}
    context = {}

    result = lambda_handler(event, context)

    assert result["statusCode"] == 200