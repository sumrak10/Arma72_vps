from fastapi import FastAPI


app = FastAPI()







from app.arma_bot.router import router as bot_router
app.include_router(bot_router)
