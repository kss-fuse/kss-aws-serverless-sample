# from unittest.mock import patch
from src.functions.init.app import lambda_handler


# @patch("src.functions.init.app.get_jwks")
# @patch("src.functions.init.app.jwt.decode")
# @patch("src.functions.init.app.jwt.get_unverified_header")
def test_lambda_handler(mock_header, mock_decode, mock_get_jwks):

    mock_get_jwks.return_value = {
        "keys": [
            {
                "kid": "test-kid",
                "kty": "RSA",
                "use": "sig",
                "n": "test",
                "e": "AQAB"
            }
        ]
    }

    mock_header.return_value = {"kid": "test-kid"}
    mock_decode.return_value = {"sub": "test-user"}

    event = {
        "headers": {
            "Authorization": "Bearer dummy-token"
        }
    }

    result = lambda_handler(event, {})

    assert result["statusCode"] == 200