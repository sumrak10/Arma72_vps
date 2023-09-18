from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='APP__')

    PROD: bool = False
    DEBUG: bool = False
    HOST: str = 'https://a2c4-84-54-80-187.ngrok-free.app'
    PORT: int = '8001'

settings = Settings()
