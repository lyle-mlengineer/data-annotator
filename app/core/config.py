from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os

load_dotenv()


class Config(BaseSettings):
    APP_NAME: str = "SautiFlow Labs"
    DEBUG: bool = True

    TEMPLATES_DIR: str = "app/ui/v1/templates"
    STATIC_DIR: str = "app/ui/v1/static"
    
    # YOUTUBE_CREDENTIALS_PATH: str = os.getenv(
    #     "YOUTUBE_CREDENTIALS_PATH", "credentials.json"
    # )
    # CLIENT_SECRET_FILE: str = os.environ.get(
    #     "CLIENT_SECRET_FILE", "C:/Users/User/Downloads/secrets.json"
    # )
    
    # DATA_DIR: str = "C:\\Datasets\\audio\\maongezi"
    
    CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")            # NEW
    # CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0")
    
    # POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    # POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "lyle")
    # POSTGRES_DB: str = os.getenv("POSTGRES_DB", "postgres")
    # POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "127.0.0.1")
    # POSTGRES_PORT: int = os.getenv("POSTGRES_PORT", 5432)
    
    MAX_AUDIO_DURATION_SECONDS: int = 30  # 15 minutes
    MIN_AUDIO_DURATION_SECONDS: int = 10  # 5 seconds


config = Config()