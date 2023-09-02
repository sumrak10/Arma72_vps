from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='APP___')

    DEBUG: bool
    HOST: str
    PORT: int

SETTINGS = Settings()