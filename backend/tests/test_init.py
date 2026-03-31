from src.functions.init.app import lambda_handler
from unittest.mock import patch

@patch("src.functions.init.app.jwt.decode")
def test_lambda_handler(mock_decode):
    mock_decode.return_value = {"sub": "test-user"}

    event = {
        "headers": {
            "authorization": "Bearer dummy-token"
        }
    }
    context = {}

    result = lambda_handler(event, context)

    assert result["statusCode"] == 200