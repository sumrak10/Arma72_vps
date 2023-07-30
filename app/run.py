import uvicorn


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=443, ssl_keyfile="private_key.key", ssl_certfile="public_key.pem", proxy_headers=True)