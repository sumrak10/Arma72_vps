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
async def consultation_handler(msg: types.Message) -> None:
    wsroom = ws_service.get_WSRoom_by_manager_id(msg.from_user.id)
    if wsroom is not None:
        await ws_service.send_message_from_manager(msg.from_user.id, msg.text, wsroom=wsroom)


@router.callback_query(WSCallbackData.filter())
async def ws_webhook_callback(query: types.CallbackQuery, callback_data: WSCallbackData):
    status = await ws_service.set_manager_to_room(callback_data.uid, query.from_user.id)
    if status:
        await bot.send_message(query.from_user.id, text="Онлайн консультация начата")
    else:
        await query.answer(text="В чате консультации уже есть менеджер или она уже завершена!")
