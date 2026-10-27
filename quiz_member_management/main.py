from fastapi import FastAPI
from routes.user_route import router_user
from routes.auth_route import router_auth
import uvicorn

app = FastAPI(
    title='회원 관리',
    description='사용자 회원가입 및 CRUD API',
    version='1.0.0'
)

app.include_router(router_user)
app.include_router(router_auth)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )