import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from settings import SETTINGS as APP_SETTINGS

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")

    APP_PREFIX: str = "/arma_bot"
    TOKEN: str = os.getenv("TOKEN")
    WEBHOOK_PATH: str = f"{APP_PREFIX}/{TOKEN}"
    WEBHOOK_URL: str =  f"{APP_SETTINGS.HOST}:{APP_SETTINGS.PORT}{WEBHOOK_PATH}"

SETTINGS = Settings()