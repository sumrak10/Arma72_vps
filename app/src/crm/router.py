from fastapi import APIRouter

from ._bot import bot
from .schemas.orders import OrderSchema


router = APIRouter(
    prefix='/crm'
)

@router.post('/order')
async def notify_new_order(order: OrderSchema):
    # bot.send_message()
    print(order)