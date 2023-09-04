from aiogram import Router, F
from aiogram import types

from .._bot import bot

from .callbacks_data import WSCallbackData
from .services import ws_service


router = Router(name="chat_widget")

@router.message(F.text == '/stop')
async def end_consultation_handler(msg: types.Message) -> None:
    ws_service.disconnect()
    await msg.answer("Онлайн консультация завершена!")


@router.message(F.text)
async def end_consultation_handler(msg: types.Message) -> None:
    await msg.answer("Это просто текст")


@router.callback_query(WSCallbackData.filter())
async def ws_webhook_callback(query: types.CallbackQuery, callback_data: WSCallbackData):
    await bot.send_message(query.from_user.id, text="Онлайн консультация начата")
    await ws_service.set_manager_to_room(callback_data.uid, query.from_user.id)
