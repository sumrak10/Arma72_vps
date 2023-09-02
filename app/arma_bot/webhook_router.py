import logging

from fastapi import APIRouter

from aiogram import types, Dispatcher, Bot

from .bot import bot, dp
from arma_bot.settings import SETTINGS



router = APIRouter()



@router.post(SETTINGS.WEBHOOK_PATH)
async def bot_webhook(update: dict):
    logging.warn("updates getted")
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)

@router.on_event("startup")
async def on_startup():
    logging.warn("Bot on startup event")
    webhook_info = await bot.get_webhook_info()
    f = open('rootCA.pem', 'rb')
    cert = f.read()
    f.close()
    if webhook_info.url != SETTINGS.WEBHOOK_URL:
        logging.warn("Bot webhook setted")
        await bot.set_webhook(
            url=SETTINGS.WEBHOOK_URL,
            certificate=cert
        )

@router.on_event("shutdown")
async def on_shutdown():
    logging.info('Bot shutdown event')
    
    await bot.delete_webhook()
    session = await bot.get_session()
    await session.close()