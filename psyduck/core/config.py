import os
import dotenv
from pydantic import BaseSettings


dotenv.load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Fast Project'
    VERSION: str = '0.1.0'
    db_driver: str = os.getenv('SQL_DRIVER')
    db_url: str = f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}" \
                  f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}" if db_driver == 'pg' else 'sqlite:///./sql_app.db'
    TEST_DATABASE_URL: str = f"postgresql+asyncpg://{os.getenv('POSTGRES_USER_TEST')}:{os.getenv('POSTGRES_PASSWORD_TEST')}" \
                             f"@{os.getenv('POSTGRES_HOST_TEST')}:{os.getenv('POSTGRES_PORT_TEST')}/{os.getenv('POSTGRES_DB_TEST')}"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', default=30)
    SECRET_KEY: str = os.getenv('SECRET_KEY', default="secret_key")
    ALGORITHM: str = os.getenv('ALGORITHM', default="HS256")


settings = Settings()