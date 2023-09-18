import logging

from fastapi import APIRouter
from aiogram.dispatcher.dispatcher import Dispatcher
from .bot.ag_router import router as handlers_router
from .chat_widget.ag_router import router as chat_widget_router
from .router import router as crm_router

from .FastAPIRequestHandler import FastAPIRequestHandler
from .config import settings
from ._bot import bot



dp = Dispatcher()


dp.include_router(handlers_router)

dp.include_router(chat_widget_router)



router = APIRouter(
    prefix=settings.APP_PREFIX, 
    tags=['bot']
)


webhook_requests_handler = FastAPIRequestHandler(
    dispatcher=dp, 
    bot=bot, 
    webhook_url=settings.WEBHOOK_URL,
    webhook_path=settings.WEBHOOK_PATH,
    handle_in_background=False
)
router.include_router(webhook_requests_handler.get_router())

router.include_router(crm_router)