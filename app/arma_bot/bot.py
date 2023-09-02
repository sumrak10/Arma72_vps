import logging

from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from .users.auth import get_current_user
from .users.models import TelegramUser
from .CRM.keyboards import buildMainMenuKeyBoard
from .CRM.models import Order

from arma_bot.settings import SETTINGS



bot = Bot(token=SETTINGS.TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())




@dp.message_handler(commands=['start'])
async def start_handler(msg: types.Message):
    # user = await get_current_user(msg)
    # if msg.get_args():
    #     await start_args_director(msg, user)
    # await msg.reply(f"Здравствуйте, {user.first_name} {user.last_name}!\nЧем могу помочь?", reply_markup=await buildMainMenuKeyBoard(user))
    await msg.reply(f"Данный функционал еще находится в разработке")

@dp.message_handler(commands=['menu'])
async def start_handler(msg: types.Message):
    # user = await get_current_user(msg)
    # await msg.reply(f"Аккаунт: {user.first_name} {user.last_name}!\nГлавное меню:", reply_markup=await buildMainMenuKeyBoard(user))
    await msg.reply(f"Данный функционал еще находится в разработке")

@dp.message_handler(commands=['help'])
async def start_handler(msg: types.Message):
    await msg.reply("/menu - Главное меню\n/help - Выводит данное сообщение")


# async def start_args_director(msg: types.Message, user: TelegramUser) -> None:
#     separator: str = '_'
#     command: str = msg.get_args().split(separator,1)[0]
#     values: list = msg.get_args().split(separator,1)[1].split(separator)
#     if command == 'link_the_order_to_me':
#         order = await Order.query.where(Order.id==values[0]).gino.first()
#         await order.update(
#             telegram_user = user.id
#         ).apply()
#     else:
#         msg.reply("Вы перешли по не рабочей ссылке!")