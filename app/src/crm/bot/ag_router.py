####################################################################################################

from aiogram import types
from aiogram import Router
from aiogram import F

from .._bot import bot

from ..config import settings


router = Router(name='main')


@router.message(F.text == '/start')
async def start(msg: types.Message) -> None:
    await msg.reply(f"✨ Бот поддержки сайта Arma72.com\nВаш id: {msg.from_user.id} {settings.GROUP_ID}")



@router.message(F.photo)
async def photo_handler(msg: types.Message) -> None:
    # await bot.send_photo(msg.from_user.id, photo=types.FSInputFile
    # (path='/app/src/anocat/bot/1.png'))
    # file = await bot.get_file(msg.photo[0].file_id)
    # logging.warn(file.file_path)
    # await bot.send_photo(msg.from_user.id, photo = msg.photo[0].file_id)
    pass