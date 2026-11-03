from passlib.context import CryptContext

#비밀번호 해싱(암호화) 설정
# CryptContext: 비밀번호를 해싱하고 검증하는 도구 묶음
# bcrypt: 사용할 해시 알고리즘. 느리게 설계되어 있고 salt(무작위 문자열)가 자동으로 붙음
pwd_context = CryptContext(schemes=['bcrypt'])

class HashPassword:
    def create_hash(self, password: str):
        return pwd_context.hash(password)

    def verify_hash(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)