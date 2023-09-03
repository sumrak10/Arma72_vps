from fastapi import APIRouter

from .schemas.orders import OrderSchema


router = APIRouter(
    prefix='/crm'
)

@router.post('/order')
async def notify_new_order(order: OrderSchema):
    