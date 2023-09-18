import uvicorn

from src.config import settings


if __name__ == '__main__':
    if settings.PROD:
        uvicorn.run("src.main:app", 
            host='0.0.0.0', 
            port=settings.PORT, 
            ssl_keyfile="./letsencrypt/live/arma72vps.ru/privkey.pem", 
            ssl_certfile="./letsencrypt/live/arma72vps.ru/fullchain.pem"
        )
    else:
        uvicorn.run("src.main:app", 
            host='0.0.0.0', 
            port=settings.PORT
        )