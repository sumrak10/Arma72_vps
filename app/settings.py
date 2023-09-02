from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='APP___', env_nested_delimiter='__')

    DEBUG: bool
    HOST: str
    PORT: int

SETTINGS = Settings()

import logging
logging.warning(SETTINGS.model_dump())