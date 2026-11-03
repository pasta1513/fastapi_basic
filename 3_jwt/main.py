from fastapi import FastAPI
import uvicorn
from routes.user_router import user_router

app = FastAPI()
app.include_router(user_router, prefix='/users')

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=['*'], # ['http://localhost:3000', '...']
    allow_methods=['*'],
    allow_headers=['*']
)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8080, reload=True)