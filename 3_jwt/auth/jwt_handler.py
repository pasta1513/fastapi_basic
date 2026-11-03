import time
from jose import jwt, JWTError, ExpiredSignatureError
from fastapi import HTTPException, status

SECRET_KEY = '비밀 키'

def create_access_token(id: str):
    payload = {
        'user': id,
        'exp': time.time() + 30 # 10초 후 토큰 만료
    }

    # Header.Payload.Signature
    # payload(토큰에 담을 데이터)를 SECRET_KEY로 서명해서 JWT 문자열 하나를 만듦
    # algorithm='HS256': 서명 방식. HMAC + SHA-256. 같은 키로 서명하고 같은 키로 검증하는 방식
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='토큰 만료. 인증 먼저 해주세요.'
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='잘못된 요청입니다.'
        )