from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str
    database_url: str
    secret: str
    domain: str

    class Config:
        env_file = '.env'


settings = Settings()
