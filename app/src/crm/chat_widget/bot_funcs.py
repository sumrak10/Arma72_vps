from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .callbacks_data import WSCallbackData
from .._bot import bot
from ..config import settings



async def invite_manager_in_room(uid:str, message: str) -> types.Message:
    text = "🔥 Запрос на онлайн консультацию!\n"
    text += f"❔ Текст запроса: {message}\n"
    text += "Ⓜ️ Менеджер: Отсутсвует"
    #  url="https://t.me/arma72_bot"
    btn = InlineKeyboardButton(
        text="🚩 Соединиться", 
        callback_data=WSCallbackData(uid=uid).pack()
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[btn]])
    return await bot.send_message(settings.GROUP_ID, text, reply_markup=kb)


async def send_message_to_manager(id: int, text: str) -> types.Message:
    return await bot.send_message(id, text)