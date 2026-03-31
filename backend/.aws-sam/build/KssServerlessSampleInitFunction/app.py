import os
import json
import requests
from jose import jwt
from jose.exceptions import JWTError

# ===== 設定 =====
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
API_AUDIENCE = "https://kss-api"
ALGORITHMS = ["RS256"]

# ===== JWKSキャッシュ =====
_jwks = None

def get_jwks():
    global _jwks

    if _jwks is None:
        if not AUTH0_DOMAIN:
            raise ValueError("AUTH0_DOMAIN is not set")

        jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
        _jwks = requests.get(jwks_url).json()

    return _jwks

def lambda_handler(event, context):
    try:
        # ===== ヘッダ取得 =====
        headers = event.get("headers", {})
        auth_header = headers.get("authorization") or headers.get("Authorization")

        if not auth_header:
            raise Exception("Authorization header is missing")

        token = auth_header.split(" ")[1]

        # ===== ヘッダからkid取得 =====
        unverified_header = jwt.get_unverified_header(token)

        rsa_key = {}
        jwks = get_jwks()
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }

        if not rsa_key:
            raise Exception("Unable to find appropriate key")

        # ===== JWT検証 =====
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=ALGORITHMS,
            audience=API_AUDIENCE,
            issuer=f"https://{AUTH0_DOMAIN}/"
        )

        # ===== 成功レスポンス =====
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "JWT is valid",
                "user": payload
            })
        }

    except JWTError as e:
        return {
            "statusCode": 401,
            "body": json.dumps({
                "message": "Invalid token",
                "error": str(e)
            })
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Error processing request",
                "error": str(e)
            })
        }