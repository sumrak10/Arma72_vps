from aiogram import Router, F
from aiogram import types
from aiogram.exceptions import TelegramForbiddenError

from .._bot import bot

from . import exceptions
from ..config import settings
from .callbacks_data import WSCallbackData
from .services import ws_service


router = Router(name="chat_widget")

@router.message(F.text == '/stop')
async def end_consultation_handler(msg: types.Message) -> None:
    await ws_service.close_ws_by_manager(msg.from_user.id)


@router.message(F.text)
async def consultation_handler(msg: types.Message) -> None:
    wsroom = ws_service.get_WSRoom_by_manager_id(msg.from_user.id)
    if wsroom is not None:
        await ws_service.send_message_from_manager(
            msg.from_user.id, msg.text, 
            wsroom=wsroom
        )


@router.callback_query(WSCallbackData.filter())
async def ws_webhook_callback(query: types.CallbackQuery, callback_data: WSCallbackData):
    try:
        wsroom = await ws_service.set_manager_to_room(
            uid=callback_data.uid, 
            manager_id=query.from_user.id, 
            manager_name=query.from_user.full_name
        )
    except TelegramForbiddenError:
        await query.answer("Нет активного чата с ботом")
    except exceptions.UserNowInOtherRoom:
        await query.answer("Вы находитесь в другой консультации,\
завершите ее и попробуйте снова!")
    except exceptions.RoomNotFound:
        await query.answer("Онлайн консультация завершена!")
    except exceptions.OtherManagerConnectedRoom:
        await query.answer("Другой менеджер уже находится в чате")
    except Exception:
        await query.answer("Произошла непредвиденная ошибка, свяжитесь с разработчиком")
    else:
        await bot.edit_message_text(
            text=f"🌀 Онлайн консультация в процессе\n❔ Текст запроса: {wsroom.text}\nⓂ️ Менеджер: {query.from_user.full_name}", 
            chat_id=settings.GROUP_ID, 
            message_id=query.message.message_id
        )
        await bot.send_message(query.from_user.id, text=f"❔ Текст запроса: {wsroom.text}")
