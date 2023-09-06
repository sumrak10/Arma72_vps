import uvicorn

from src.config import settings


if __name__ == '__main__':
    uvicorn.run("src.main:app", host='0.0.0.0', port=settings.PORT, ssl_keyfile="rootCA.key", ssl_certfile="rootCA.pem")
    # uvicorn.run("src.main:app", host='0.0.0.0', port=settings.PORT)