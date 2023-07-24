from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

bot_app = FastAPI()

bot_app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["localhost"] 
)

from .CRM.router import router as crm_router
bot_app.include_router(crm_router, prefix="/crm")