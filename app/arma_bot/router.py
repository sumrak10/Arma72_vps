from fastapi import APIRouter
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from arma_bot.settings import SETTINGS



router = APIRouter(
    prefix=SETTINGS.BOT_PREFIX
)

# bot_app.add_middleware(
#     TrustedHostMiddleware, allowed_hosts=["localhost"] 
# )


# from database.events import router as database_events_router
# app.include_router(database_events_router)


from .webhook_router import router as webhook_router
router.include_router(webhook_router)

from .CRM.router import router as crm_router
router.include_router(crm_router)

from .chat_widget.router import router as chat_widget_router
router.include_router(chat_widget_router)