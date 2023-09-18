from fastapi import FastAPI

from .crm.main import router as bot_webhook_router


app = FastAPI()



app.include_router(bot_webhook_router)