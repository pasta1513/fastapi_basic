from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from auth.jwt_handler import verify_access_token

api_key_header = APIKeyHeader(name = 'Authorization')

async def authenticate(token: str = Security(api_key_header)):
    #token = Bearer token 정보
    if ' ' in token:
        token = token.split(' ')[1]
    payload = verify_access_token(token)
    print('authenticate payload: ', payload)

    return payload['user']