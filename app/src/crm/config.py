from pydantic_settings import BaseSettings, SettingsConfigDict

from ..config import settings as app_settings

class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='BOT__')

    TOKEN: str
    APP_PREFIX: str = "/bot"


settings = Settings()

WEBHOOK_URL = f"{app_settings.HOST}{settings.APP_PREFIX}/webhook_updates"
WEBHOOK_PATH = f"/webhook_updates"
GROUP_ID = -912505080 # test group
# GROUP_ID = -1001640394603 # prod group