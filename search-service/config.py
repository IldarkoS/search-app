from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    log_level: str = Field(default="INFO")

    # MinIO
    minio_endpoint: str
    minio_access_key: str
    minio_secret_key: str
    minio_bucket_name: str

    embedding_model_name: str = Field(default="sentence-transformers/all-MiniLM-L6-v2")

    # Qdrant
    qdrant_host: str
    qdrant_port: int
    qdrant_collection: str

    class Config:
        env_file = ".env"

settings = Settings()
