

from fastapi import APIRouter
from fastapi import Request
from fastapi import Depends
from fastapi.responses import JSONResponse


from bot.bot import bot
from .settings import SALES_MANAGERS_GROUP_ID

from .schemas import OrderSchema, ProductInOrderSchema, ConsultationSchema



router = APIRouter()



@router.get("/")
async def index():
    return JSONResponse({"message": "Hello from bot"})

@router.get("/test")
async def index():
    await bot.send_message(SALES_MANAGERS_GROUP_ID, "test")
    return JSONResponse({"message": "sended"})

@router.post("/order")
async def new_order_notification(order: OrderSchema):
    await bot.send_message(SALES_MANAGERS_GROUP_ID, f"Новая заявка!\n<a href='https://arma72.com/admin/CRM/order/{order.id}/change/'>Ссылка</a>", parse_mode="HTML")
    return JSONResponse({"message": "order_created"})


@router.post("/consultation")
async def new_consultation_notification(consultation: ConsultationSchema):
    text = "Запрос на консультацию:\n"
    if consultation.name:
        text += f"Имя клиента: {consultation.name}\n"
    text += f"Контакты: {consultation.contacts}\n"
    if consultation.text:
        text += f"Сопровождающий текст: {consultation.text}\n"
    await bot.send_message(SALES_MANAGERS_GROUP_ID, text)
    return JSONResponse({"message": "consultation created"})
