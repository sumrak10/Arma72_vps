from fastapi import FastAPI


app = FastAPI()



# from database.events import router as database_events_router
# app.include_router(database_events_router)


from bot.config import BOT_APP_PREFIX
from bot.main import bot_app
app.mount(BOT_APP_PREFIX, bot_app)