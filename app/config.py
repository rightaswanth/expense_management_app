from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Expense API"


settings = Settings()