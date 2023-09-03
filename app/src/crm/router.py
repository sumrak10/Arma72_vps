from fastapi import APIRouter

from ._bot import bot

from .schemas.orders import OrderSchema

from .config import GROUP_ID

router = APIRouter(
    prefix='/crm'
)

@router.post('/order')
async def notify_new_order(order: OrderSchema):
    bot.send_message(GROUP_ID, order.model_dump_json())