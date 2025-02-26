from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str
    database_url: str
    secret: str
    domain: str = '127.0.0.1:8000'

    class Config:
        env_file = '.env'


settings = Settings()
