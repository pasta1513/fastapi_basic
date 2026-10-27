from fastapi import FastAPI, APIRouter, Query
from pydantic import BaseModel

app = FastAPI()
router = APIRouter()

class Item(BaseModel):
    name: str
    price: int
    count:int

@router.post('/items')
def add_item(item: Item):
    msg = item.name + ' 등록 완료'
    total = item.price * item.count
    return {'msg': msg, 'total': total}

items = [
    Item(name = '떡볶이',
         price = 3000,
         count = 10),
    Item(name = '순대',
         price = 4000,
         count = 10),
    Item(name = '김밥',
         price = 2500,
         count = 10),
]

@router.get('/items/{name}')
def get_item(name: str):
    for i in items:
        if i.name == name:
            # return {'name': name, 'price': i.price, 'count': i.count}
            return i.model_dump()

    return {'msg': '상품이 없습니다.'}

@router.get('/search')
def search_item(max_price: int = Query(5000, description='최대 가격')):
    result= []

    for i in items:
        if i.price <= max_price:
            result.append(i.model_dump())

    return result

app.include_router(router = router)