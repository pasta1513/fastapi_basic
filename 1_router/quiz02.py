from fastapi import FastAPI, APIRouter

app = FastAPI(title='분식집 API', version='0.0.1')
router = APIRouter(tags=['메뉴'])

@router.get('/menu')
def menu_get():
    return {'msg': '메뉴 보기'}

@router.post('/menu')
def menu_post():
    return {'msg': '메뉴 추가'}

@router.put('/menu')
def menu_put():
    return {'msg': '메뉴 수정'}

@router.delete('/menu')
def menu_delete():
    return {'msg': '메뉴 삭제'}

app.include_router(router = router)