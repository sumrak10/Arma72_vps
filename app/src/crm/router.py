from fastapi import APIRouter

from ._bot import bot

from .schemas.orders import OrderSchema

from .config import GROUP_ID

router = APIRouter(
    prefix='/crm'
)

@router.post('/order')
async def notify_new_order(order: OrderSchema):
    text = f"🔴 {order.created_at} Новая заявка на сумму {order.summ} р.\n"
    text += f"📞 Контакты: {order.contacts}"
    for product in order.products:
        text += f"- <a href='https://arma72.com/admin/shop/product/{product.id}/change/'>{product.name}</a>   Кол-во: {product.count}   Сумма: {product.summ}\n"
    text += f"👁 <a href='https://arma72.com/admin/CRM/order/{order.id}/change/'>Открыть в админ панели</a>"
    await bot.send_message(GROUP_ID, text, parse_mode="HTML")