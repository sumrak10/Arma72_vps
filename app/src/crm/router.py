from fastapi import APIRouter

from ._bot import bot

from .schemas.orders import OrderSchema
from .schemas.consultations import ConsultationSchema

from .config import GROUP_ID

router = APIRouter(
    prefix='/crm'
)

from .chat_widget.router import router as chat_widget_router
router.include_router(chat_widget_router)

@router.post('/order')
async def notify_new_order(order: OrderSchema):
    text = f"🔴 Новая заявка на сумму {order.summ} р.\n🕘 Создана: {order.created_at}\n"
    text += f"📞 Контакты: <code>{order.contacts}</code>\n\n"
    for product in order.products:
        text += f"⭕️ <a href='https://arma72.com/admin/shop/product/{product.id}/change/'>{product.name}</a>\n- Кол-во: {product.count}\n- Сумма: {product.summ}\n"
        if product.options != "None":
            text += f"- Опция: {product.options}\n"
        text += "\n"
    text += f"👁 <a href='https://arma72.com/admin/CRM/order/{order.id}/change/'>Посмотреть в админ панели</a>"
    await bot.send_message(GROUP_ID, text, parse_mode="HTML")

@router.post("/consultation")
async def notify_new_consultation(consultation: ConsultationSchema):
    text = "🔴 Новая завка на консультацию!\n"
    text = f"📞 Контакты: <code>{consultation.contacts}</code>\n"
    if consultation.name != "Отсутствует":
        text += f"🔰 Имя: {consultation.name}\n"
    if consultation.text != "Отсутствует":
        text += f"🔰 Текст: {consultation.text}\n"
    await bot.send_message(GROUP_ID, text, parse_mode="HTML")