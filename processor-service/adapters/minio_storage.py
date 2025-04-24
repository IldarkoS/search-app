from loguru import logger
from minio import Minio
from minio.error import S3Error
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from config import settings
from ports.file_storage import FileStorageInterface

MAX_FILE_SIZE = 50 * 1024 * 1024


class MinioStorageAdapter(FileStorageInterface):
    def __init__(self):
        self.client = Minio(
            settings.minio_endpoint,
            access_key=settings.minio_access_key,
            secret_key=settings.minio_secret_key,
            secure=False
        )
        self.bucket = settings.minio_bucket_name

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type(S3Error)
    )
    def download(self, path: str) -> bytes:
        logger.info("Downloading file '{}' from bucket '{}'", path, self.bucket)
        try:
            stat = self.client.stat_object(self.bucket, path)
            if stat.size > MAX_FILE_SIZE:
                raise ValueError(f"File {path} exceeds max allowed size: {stat.size} bytes")

            response = self.client.get_object(self.bucket, path)
            data = response.read()
            response.close()
            response.release_conn()

            logger.info("Successfully downloaded {} ({} bytes)", path, len(data))
            return data

        except S3Error as e:
            if e.code == "NoSuchKey":
                logger.warning("File not found in MinIO: {}", path)
            else:
                logger.exception("S3Error while downloading file: {}", e)
            raise
        except Exception as e:
            logger.exception("Failed to download file '{}': {}", path, e)
            raise