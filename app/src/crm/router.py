from fastapi import APIRouter

from ._bot import bot

from .schemas.orders import OrderSchema

from .config import GROUP_ID

router = APIRouter(
    prefix='/crm'
)

@router.post('/order')
async def notify_new_order(order: OrderSchema):
    text = f"❗️ Новая заявка на сумму {order.summ} р.\n🔴 Созданан: {order.created_at}\n"
    text += f"📞 Контакты: {order.contacts}\n\n"
    for product in order.products:
        text += f"⭕️ <a href='https://arma72.com/admin/shop/product/{product.id}/change/'>{product.name}</a>\n- Кол-во: {product.count}\n- Сумма: {product.summ}\n\n"
    text += f"👁 <a href='https://arma72.com/admin/CRM/order/{order.id}/change/'>Посмотреть в админ панели</a>"
    await bot.send_message(GROUP_ID, text, parse_mode="HTML")