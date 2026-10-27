from fastapi import FastAPI
from fastapi import APIRouter
# 데이터 검증
from pydantic import BaseModel

from fastapi import Path

class User(BaseModel):
    name: str
    age: int
    addr: str

app = FastAPI(title='test FastAPI',
              description='부연 설명',
              version='1.1')
# 서버 실행: python -m uvicorn ex01:app --port 8000 --reload
router = APIRouter(tags=['회원 관리'])
router_agent = APIRouter(tags=['에이전트'])

@router.get('/test')
def test():
    return {'msg': '데이터 요청'}

@router_agent.post('/test')
def test(user:User):
    return {'msg': f'데이터 추가: {user}'}

@router_agent.put('/test')
def test():
    return {'msg': '데이터 수정'}

@router.delete('/test')
def test():
    return {'msg': '데이터 삭제'}

users = [
    User(name = '홍길동',
         age = 10,
         addr = '산골짜기'),
    User(name = '김개똥',
         age = 20,
         addr = '개똥별'),
    User(name = '고길동',
         age = 10,
         addr = '쌍문동'),
]

@router.get('/api/users')
def get_users():
    print(users)
    return {'users': users}

# {name}은 경로 매개변수(Path Parameter)로, 필수 사항(required)이다.
@router_agent.get('/api/path/{name}')
# =Path(...): "이 매개변수는 URL 경로에서 가져온다"는 것을 명시하고, 추가 설정을 붙이는 함수
# 첫 번째 인자는 기본값 자리이고, ...는 기본값 없음/필수 값이라는 뜻
# 경로 매개변수는 원래 항상 필수라서 생략해도 결과는 같습니다. Path(description='...')만 써도 됨
# description=''은 설명 문구, 동작 영향 x, 문서용
def get_users(name: str = Path(..., description='input user name')):
    print('name:', name)
    for u in users:
        if u.name == name:
            return {'user': u}
    return {'user': '존재하지 않는 사용자입니다.'}

from fastapi import Query

@router_agent.get('/api/path')
def get_users(name: str = Query('홍길동', description='input user name')):
    print('name:', name)
    for u in users:
        if u.name == name:
            return {'user': u}
    return {'user': '존재하지 않는 사용자입니다.'}

app.include_router(router=router)
app.include_router(router=router_agent)