from fastapi import APIRouter



router = APIRouter(
    prefix='/crm'
)

@router.post('/order')
async def notify_new_order():
    pass