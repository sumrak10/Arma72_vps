import logging

from fastapi import APIRouter
from aiogram.dispatcher.dispatcher import Dispatcher

from .FastAPIRequestHandler import FastAPIRequestHandler
from .config import settings, WEBHOOK_URL, WEBHOOK_PATH
from ._bot import bot



dp = Dispatcher()


from .bot.ag_router import router as handlers_router
dp.include_router(handlers_router)

from .chat_widget.ag_router import router as chat_widget_router
dp.include_router(chat_widget_router)



router = APIRouter(
    prefix=settings.APP_PREFIX, 
    tags=['bot']
)


# webhook_requests_handler = FastAPIRequestHandler(
#     dispatcher=dp, 
#     bot=bot, 
#     webhook_url=WEBHOOK_URL,
#     webhook_path=WEBHOOK_PATH,
#     handle_in_background=False
# )
# router.include_router(webhook_requests_handler.get_router())

from .router import router as crm_router
router.include_router(crm_router)