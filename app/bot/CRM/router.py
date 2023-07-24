from typing import Annotated

from fastapi import APIRouter
from fastapi import Request
from fastapi import Depends
from fastapi.responses import JSONResponse


from bot.bot import bot
from .config import SALES_MANAGERS_GROUP_ID

from .schemas import OrderSchema, ProductInOrderSchema, AppealSchema



router = APIRouter()



@router.get("/")
async def index():
    return JSONResponse({"message": "Hello from bot"})

@router.get("/test")
async def index():
    await bot.send_message(SALES_MANAGERS_GROUP_ID, "test")
    return JSONResponse({"message": "sended"})

@router.post("/create_order")
async def new_order_notification(order: OrderSchema):
    return JSONResponse({"message": "order_created"})

@router.post("/add_in_order")
async def new_order_notification(order: ProductInOrderSchema):
    await bot.send_message(SALES_MANAGERS_GROUP_ID, f"Order from {order.name} summ {order.summ}")

@router.post("/create_appeal")
async def new_order_notification(order: AppealSchema):
    return JSONResponse({"message": "appeal created"})
