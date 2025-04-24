from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    log_level: str = Field(default="INFO")

    # Kafka
    kafka_bootstrap_servers: str
    kafka_topic: str

    # MinIO
    minio_endpoint: str
    minio_access_key: str
    minio_secret_key: str
    minio_bucket_name: str

    # Vector DB / PostgreSQL
    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str

    embedding_model_name: str = Field(default="sentence-transformers/all-MiniLM-L6-v2")

    # Qdrant
    qdrant_host: str
    qdrant_port: int
    qdrant_collection: str

    class Config:
        env_file = ".env"

settings = Settings()
