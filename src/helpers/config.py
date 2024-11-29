from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    URL: str
    DB_NAME: str
    USERNAME: str
    ODOO_API_KEY: str

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()

