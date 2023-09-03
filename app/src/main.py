from fastapi import FastAPI


app = FastAPI()



from .crm.main import router as bot_webhook_router
app.include_router(bot_webhook_router)