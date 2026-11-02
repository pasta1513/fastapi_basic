from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from schemas.user_schemas import User
from schemas.user_update_schemas import UserUpdate
from db import user_db
from db.connection import get_db

user_router = APIRouter(tags=['User'])

@user_router.get('/test')
async def test() -> dict:
    return {'msg':'test'}

@user_router.get('/')
async def get_users(db: Session = Depends(get_db)):
    users = await user_db.select_users(db)
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
async def create_user(user: User, db: Session = Depends(get_db)) -> User:
    # print('사용자 추가 router: ', user)
    result = await user_db.insert(user, db)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='중복된 email입니다.'
        )
    
    return user

from schemas.user_update_schemas import UserUpdate
from fastapi import Form

@user_router.put("/form/{username}") # users/form/{사용자id}
async def update_user(username:str, user:UserUpdate=Form(...), db:Session=Depends(get_db)):
    result = await user_db.update(username, user, db)

    if result:
        return result
    raise HTTPException(
        status_code=404, 
        detail="수정 사용자 id 없음!!!"
    )

@user_router.put('/{username}')
async def update_user(username: str, user: UserUpdate, db: Session = Depends(get_db)) -> User:
    # print(username, user)
    result = await user_db.update(username, user, db)

    if result:
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='수정된 사용자가 없습니다.'
    )

@user_router.delete('/{username}')
async def delete_user(username: str, db: Session = Depends(get_db)) -> User:
    result = await user_db.delete(username, db)

    if result:
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='사용자를 찾지 못하였습니다.'
    )