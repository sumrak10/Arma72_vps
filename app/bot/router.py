from fastapi import APIRouter
from fastapi.responses import JSONResponse

from bot.bot import bot
from .config import MAIN_GROUP_ID

from .schemas import OrderSchema


router = APIRouter()



@router.get("/")
async def index():
    return JSONResponse({"message": "Hello from bot"})

@router.post("/new_order_notification")
async def new_order_notification(order: OrderSchema):
    await bot.send_message(MAIN_GROUP_ID, f"Order from {order.name} summ {order.summ}")