from fastapi import FastAPI


app = FastAPI()



from bot.webhook_router import router as bot_webhook_router
app.include_router(bot_webhook_router)

from bot.router import router as bot_router
app.include_router(bot_router)

