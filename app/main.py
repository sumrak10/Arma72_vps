from fastapi import FastAPI


app = FastAPI()







from arma_bot.main import router as bot_router
app.include_router(bot_router)
