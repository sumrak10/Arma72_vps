import logging

from fastapi import APIRouter

from aiogram import types, Dispatcher, Bot

from .bot import bot, dp
from .config import WEBHOOK_URL, WEBHOOK_PATH



router = APIRouter()



@router.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    logging.info("telegram send updates!")
    await dp.process_update(telegram_update)


@router.on_event("startup")
async def on_startup():
    logging.info("Bot on startup event")

    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )

@router.on_event("shutdown")
async def on_shutdown():
    logging.info('Bot shutdown event')
    
    await bot.delete_webhook()
    session = await bot.get_session()
    await session.close()