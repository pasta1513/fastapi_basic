from fastapi import APIRouter, HTTPException, status
from pydantic import EmailStr
from schemas.auth_schema import UserSingIn
import db

router_auth = APIRouter(tags=['Login'], prefix='/auth')

@router_auth.post('/signin')
async def sign_in(email: EmailStr, pw: str):
    user, error = await db.sign_in(email, pw)

    if error == "wrong_email":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='존재하지 않는 회원입니다.'
        )

    if error == "wrong_pw":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='잘못된 비밀번호입니다.'
        )

    return f'{user.user_name}님, 안녕하세요.'