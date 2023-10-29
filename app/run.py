import uvicorn

from src.config import settings


if __name__ == '__main__':
    if settings.PROD:
        uvicorn.run("src.main:app", 
            host='0.0.0.0', 
            port=settings.PORT, 
            ssl_keyfile=settings.SSL_KEYFILE, 
            ssl_certfile=settings.SSL_CERTFILE
        )
    else:
        uvicorn.run("src.main:app", 
            host='0.0.0.0', 
            port=settings.PORT
        )