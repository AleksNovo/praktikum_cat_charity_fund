from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Сервис пожертвований'
    app_description: str = 'Пожертвования котикам'
    database_url: str = 'sqlite+aiosqlite:///./qrkot.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
