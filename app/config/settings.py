import os
from dotenv import load_dotenv
from pydantic import Extra
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    load_dotenv()

    # Security
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    HASHING_ALGORITHM: str = os.environ.get("HASHING_ALGORITHM")

    # DB Settings
    DB_USER: str = os.environ.get("MYSQLUSER")
    DB_PASSWORD: str = os.environ.get("MYSQLPASSWORD")
    DB_SERVER: str = os.environ.get("MYSQLHOST")
    DB_PORT: int = os.environ.get("MYSQLPORT")
    DB: str = os.environ.get("MYSQLDATABASE")

    class Config:
        env_file = ".env"
        extra = Extra.allow

    @property
    def POSTGRES_URL(self):
        url = f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_SERVER}:{self.DB_PORT}/{self.DB}"
        return url


settings = Settings()
