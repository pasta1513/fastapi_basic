from fastapi import APIRouter

user_router = APIRouter(tags=['User'])
data_set: list = []

@user_router.post('/signup')
async def sign_up(user: dict):
    data_set.append(user)
    
    return data_set