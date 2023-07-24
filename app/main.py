from fastapi import FastAPI


app = FastAPI()



from database.events import router as database_events_router
app.include_router(database_events_router)



from bot.webhook_router import router as bot_webhook_router
app.include_router(bot_webhook_router)

from bot.main import bot_app
app.mount("/bot", bot_app)