from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get('/hello')
def hello():
    return {'msg': '안녕하세요'}

@router.get('/bye')
def bye():
    return {'msg': '안녕히 가세요'}

@router.get('/calc')
# def calc(a:int, b:int):
def calc():
    a = 7
    b = 8
    sum = a + b
    mul = a * b
    return {'a': a, 'b': b, 'sum': sum, 'mul': mul}

app.include_router(router = router)