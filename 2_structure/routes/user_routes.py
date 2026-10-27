from fastapi import APIRouter, HTTPException, status
from schemas.user_schemas import User
from db import user_db

user_router = APIRouter(tags=['User'])

@user_router.get('/test')
async def test() -> dict:
    return {'msg':'test'}

@user_router.get('/')
async def get_users():
    users = await user_db.select_users()
    # print(users)
    return users

@user_router.get('/{email}')
async def get_user(email: str) -> User:
    # print('email route 연결')
    user = await user_db.select_user(email)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='존재하지 않는 사용자입니다.'
    )

@user_router.post('/',
                  response_model=User,
                  status_code=201,
                  summary='회원가입',
                  responses={409: {'description': '중복된 id입니다.'}})
async def create_user(user: User) -> User:
    # print('사용자 추가 router: ', user)
    result = await user_db.insert(user)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='중복된 email입니다.'
        )
    
    return user

@user_router.put('/{username}')
async def update_user(username: str, user: User) -> User:
    # print(username, user)
    result = await user_db.update(username, user)

    if result:
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='수정된 사용자가 없습니다.'
    )

@user_router.delete('/{username}')
async def delete_user(username: str) -> User:
    result = await user_db.delete(username)

    if result:
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='사용자를 찾지 못하였습니다.'
    )