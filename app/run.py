import uvicorn


if __name__ == '__main__':
    uvicorn.run("main:app", port=443, host='0.0.0.0', ssl_keyfile="/etc/letsencrypt/live/my_domain/privkey.pem", ssl_certfile="/etc/letsencrypt/live/my_domain/fullchain.pem")