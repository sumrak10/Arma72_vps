from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='APP__')

    PROD: bool
    DEBUG: bool
    HOST: str
    PORT: int

settings = Settings()
