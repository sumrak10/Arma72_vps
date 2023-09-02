from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

arma_bot_app = FastAPI()

# bot_app.add_middleware(
#     TrustedHostMiddleware, allowed_hosts=["localhost"] 
# )


# from database.events import router as database_events_router
# app.include_router(database_events_router)


from .webhook_router import router as webhook_router
arma_bot_app.include_router(webhook_router)

from .CRM.router import router as crm_router
arma_bot_app.include_router(crm_router)

from .chat_widget.router import router as chat_widget_router
arma_bot_app.include_router(chat_widget_router)