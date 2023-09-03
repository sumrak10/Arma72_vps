from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from sqlalchemy.orm.exc import NoResultFound

from ..main import bot
from ..schemas.topic_of_day import TopicOfDaySchema
from ..services.topic_of_day import TopicOfDayService
from ..services.users import UsersService
from ..schemas.users import UserSchema
from ._callbacks import MailsAllCallBack, MailsMineCallBack, TopicsMineCallBack, SettingsCallBack
from . import messages


async def start(msg: types.Message):
    



async def stop(msg: types.Message):
    await msg.reply(f"Good bye!")




# TODO УПРОСТИТЬ ВСЕ ДО ОБЫЧНОГО БОТА АНОНИМНЫХ ПИСЕМ