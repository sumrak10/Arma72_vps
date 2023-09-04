from pydantic_settings import BaseSettings, SettingsConfigDict

from ..config import settings as app_settings

class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='BOT__')

    TOKEN: str
    APP_PREFIX: str = "/bot"


settings = Settings()

WEBHOOK_URL = f"{app_settings.HOST}:{app_settings.PORT}{settings.APP_PREFIX}/{settings.TOKEN}"
WEBHOOK_PATH = f"/{settings.TOKEN}"
GROUP_ID = 912505080 # sxmrxk user id