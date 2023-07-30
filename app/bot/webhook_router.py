import logging

from fastapi import APIRouter

from aiogram import types, Dispatcher, Bot
from aiogram.utils.executor import start_webhook

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



async def on_startup_bot(dp):
    await bot.set_webhook(WEBHOOK_URL)
async def on_shutdown_bot(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning('Bye!')


# if __name__ == '__main__':
    


@router.on_event("startup")
async def on_startup():
    logging.info("Bot on startup event")
    await start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup_bot,
        on_shutdown=on_shutdown_bot,
        skip_updates=True,
        host="0.0.0.0",
        port=443,
    )
    # webhook_info = await bot.get_webhook_info()
    # logging.info("webhook urls:")
    # logging.info(WEBHOOK_URL)
    # logging.info(WEBHOOK_PATH)
    # if webhook_info.url != WEBHOOK_URL:
    #     await bot.set_webhook(
    #         url=WEBHOOK_URL
    #     )

# @router.on_event("shutdown")
# async def on_shutdown():
#     logging.info('Bot shutdown event')
    
#     await bot.delete_webhook()
#     session = await bot.get_session()
#     await session.close()