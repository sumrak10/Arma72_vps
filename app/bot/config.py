import os

from dotenv import load_dotenv

load_dotenv()



BOT_APP_PREFIX = "/bot"

TOKEN = os.getenv("TOKEN")

WEBHOOK_HOST = "http://194.67.65.190:80"
WEBHOOK_PATH = f"{BOT_APP_PREFIX}/{TOKEN}"
WEBHOOK_URL =  f"{WEBHOOK_HOST}{WEBHOOK_PATH}"