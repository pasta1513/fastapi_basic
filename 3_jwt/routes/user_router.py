from fastapi import APIRouter, Depends, HTTPException, status
from auth.hash_password import HashPassword
from pydantic import BaseModel
from auth.jwt_handler import create_access_token

user_router = APIRouter(tags=['User'])
data_set: list = []
hash_password = HashPassword()

@user_router.post('/signup')
async def sign_up(user: dict):
    print('변경 전 pwd: ', user['password'])
    user['password'] = hash_password.create_hash(user['password'])
    print('변경 후 pwd: ', user['password'])
    data_set.append(user)
    data_set.append({'id': 'bbb', 'password': '222'})

    return data_set

@user_router.post('/signin')
async def sign_in(user: dict):
    # db.query(user.username == User.username).find.first
    # print('user id: ', user['id'])
    # print('user pwd: ', user['password'])
    # print('db pwd: ', data_set[0]['password'])
    result = hash_password.verify_hash(user['password'], data_set[0]['password'])
    # print('비교: ', result)

    access_token = create_access_token(user['id'])
    print('token: ', access_token)

    return {'token': access_token, 'token_type': 'Bearer'}

from auth.authenticate import authenticate

@user_router.get('/info/{id}')
async def user_info(id: str, user: str = Depends(authenticate)):
    if id != user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='접근 권한이 없습니다.'
        )

    for data in data_set:
        if data['id'] == id:
            return data
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='회원 정보가 없습니다.'
    )