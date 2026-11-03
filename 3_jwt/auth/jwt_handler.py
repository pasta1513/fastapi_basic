import time
from jose import jwt

SECRET_KEY = '비밀 키'

def create_access_token(id: str):
    payload = {
        'user': id,
        'exp': time.time() + 10 # 10초 후 토큰 만료
    }

    # Header.Payload.Signature
    # payload(토큰에 담을 데이터)를 SECRET_KEY로 서명해서 JWT 문자열 하나를 만듦
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token