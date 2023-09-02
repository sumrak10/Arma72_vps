from fastapi import FastAPI


app = FastAPI()






from arma_bot.settings import SETTINGS
from arma_bot.main import arma_bot_app
app.mount(SETTINGS.APP_PREFIX, arma_bot_app)
