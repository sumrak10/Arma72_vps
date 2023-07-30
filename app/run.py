from subprocess import Popen
import os
import uvicorn



if __name__ == '__main__':
    Popen(['python', 'bot/webhook_router'])
    uvicorn.run("main:app", host='0.0.0.0', port=443, ssl_keyfile="rootCA.key", ssl_certfile="rootCA.pem")