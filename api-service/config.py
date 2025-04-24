from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    log_level: str = Field(default="INFO")

    # Kafka
    KAFKA_BOOTSTRAP_SERVERS: str
    KAFKA_TOPIC: str

    # MinIO
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_BUCKET_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()
