from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .callbacks_data import WSCallbackData
from .._bot import bot
from ..config import GROUP_ID

async def invite_manager_in_room(uid:str, message: str):
    text = "Запрос на онлайн консультацию!\n"
    text += f"Текст запроса: {message}"
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="Соединиться", url="https://t.me/arma72_bot", callback_data=WSCallbackData(uid=uid).pack()))
    await bot.send_message(GROUP_ID, text, reply_markup=kb)


async def send_message_to_manager(id: int, text: str):
    await bot.send_message(id, text)