from aiogram import Router, F
from aiogram import types

from .callbacks_data import WSCallbackData



router = Router(name="chat_widget")

@router.message(F.text == '/stop')
async def stop(msg: types.Message) -> None:
    await msg.answer("Good bye!")

@router.callback_query(WSCallbackData.filter())
async def ws_webhook_callback(query: types.CallbackQuery, callback_data: WSCallbackData):
    await query.answer(text="Вы нажали на кнопку!")
