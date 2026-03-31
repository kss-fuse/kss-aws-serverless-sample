from src.functions.init.app import lambda_handler
from unittest.mock import patch

@patch("src.functions.init.app.requests.get")
@patch("src.functions.init.app.jwt.decode")
def test_lambda_handler(mock_decode, mock_get):
    mock_decode.return_value = {"sub": "test-user"}
    mock_get.return_value.json.return_value = {"keys": []}

    event = {
        "headers": {
            "Authorization": "Bearer dummy-token"
        }
    }

    result = lambda_handler(event, {})

    assert result["statusCode"] == 200