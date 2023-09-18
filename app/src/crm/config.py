from pydantic_settings import BaseSettings, SettingsConfigDict

from ..config import settings as app_settings

class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='BOT__')

    TOKEN: str = '6615964729:AAEEPmwS1WmEKOcRZLCi286yMb5fyOKLED0'
    APP_PREFIX: str = "/bot"
    GROUP_ID: int = -912505080
    WEBHOOK_PATH: str = "/webhook_updates"
    WEBHOOK_URL: str = f"{app_settings.HOST}{APP_PREFIX}{WEBHOOK_PATH}"

settings = Settings()

