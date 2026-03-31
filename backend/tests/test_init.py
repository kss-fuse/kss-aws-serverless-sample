from src.functions.init.app import lambda_handler
from unittest.mock import patch

@patch("src.functions.init.app.requests.get")
@patch("src.functions.init.app.jwt.decode")
@patch("src.functions.init.app.jwt.get_unverified_header")
def test_lambda_handler(mock_header, mock_decode, mock_get):
    # ヘッダモック（kidを返す）
    mock_header.return_value = {"kid": "test-kid"}

    # JWTデコードモック
    mock_decode.return_value = {"sub": "test-user"}

    # JWKSモック（kid一致させる）
    mock_get.return_value.json.return_value = {
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

    event = {
        "headers": {
            "Authorization": "Bearer dummy-token"
        }
    }

    result = lambda_handler(event, {})

    assert result["statusCode"] == 200