from fastapi import FastAPI


app = FastAPI()






from arma_bot.config import BOT_APP_PREFIX
from arma_bot.main import bot_app
app.mount(BOT_APP_PREFIX, bot_app)