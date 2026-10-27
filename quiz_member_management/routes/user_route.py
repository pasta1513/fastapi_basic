from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import User
import db

router_user = APIRouter(tags=['User'], prefix='/users')

@router_user.get('/')
async def get_users():
    return await db.select_users()

@router_user.get('/{id}')
async def get_user(id: str):
    user = await db.select_user(id)

    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='존재하지 않는 회원입니다.'
    )

@router_user.post('/')
async def create_user(user: User):
    new_user = await db.insert_user(user)

    if new_user:
        return new_user
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail='이미 사용 중인 id입니다.'
    )

@router_user.put('/{id}')
async def update_user(id: str, user: User):
    updated_user, error = await db.update_user(id, user)

    if error == "not_found":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 회원입니다."
        )

    if error == "duplicate":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 사용 중인 id입니다."
        )

    return updated_user

@router_user.delete('/{id}')
async def delete_user(id: str):
    new_users = await db.delete_user(id)

    if new_users:
        return new_users
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='존재하지 않는 회원입니다.'
    )