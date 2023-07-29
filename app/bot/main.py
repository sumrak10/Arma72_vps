from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

bot_app = FastAPI()

# bot_app.add_middleware(
#     TrustedHostMiddleware, allowed_hosts=["localhost"] 
# )

from .webhook_router import router as webhook_router
bot_app.include_router(webhook_router)

from .CRM.router import router as crm_router
bot_app.include_router(crm_router, prefix="/crm")