from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from settings import SETTINGS as APP_SETTINGS


class DB(BaseModel):
    HOST:str
    PORT:int
    NAME:str
    USER:str
    PASS:str

class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='ARMA_BOT___', env_nested_delimiter='__')

    APP_PREFIX: str = "/arma_bot"
    TOKEN: str = 'NOT SETTED'
    WEBHOOK_PATH: str = f"{APP_PREFIX}/{TOKEN}"
    WEBHOOK_URL: str =  f"{APP_SETTINGS.HOST}:{APP_SETTINGS.PORT}{WEBHOOK_PATH}"

    DB: DB

SETTINGS = Settings()

import logging
logging.warning(SETTINGS.model_dump())