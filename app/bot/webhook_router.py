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
    logging.info("telegram send updates!!!!!!!!!!")
    await dp.process_update(telegram_update)

@router.on_event("startup")
async def on_startup():
    logging.info("Bot on startup event")
    webhook_info = await bot.get_webhook_info()
    logging.info(webhook_info.has_custom_certificate)
    logging.info(webhook_info.ip_address)
    logging.info(webhook_info.url)
    logging.info("webhook urls:")
    logging.info(WEBHOOK_URL)
    logging.info(WEBHOOK_PATH)
    f = open('rootCA.pem', 'rb')
    cert = f.read()
    f.close()
    if webhook_info.url != WEBHOOK_URL:
        logging.info("Bot webhook url setted")
        await bot.set_webhook(
            url=WEBHOOK_URL,
            certificate=cert
        )

@router.on_event("shutdown")
async def on_shutdown():
    logging.info('Bot shutdown event')
    
    await bot.delete_webhook()
    session = await bot.get_session()
    await session.close()