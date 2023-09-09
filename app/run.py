import uvicorn

from src.config import settings


if __name__ == '__main__':
    # uvicorn.run("src.main:app", host='0.0.0.0', port=settings.PORT, ssl_keyfile="./letsencrypt/live/arma72vps.ru/privkey.pem", ssl_certfile="./letsencrypt/live/arma72vps.ru/cert.pem", log_level="info")
    uvicorn.run("src.main:app", host='0.0.0.0', port=settings.PORT, ssl_keyfile="./rootCA.key", ssl_certfile="./rootCA.pem", log_level="info")