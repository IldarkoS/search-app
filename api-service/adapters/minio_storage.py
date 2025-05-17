from urllib.parse import quote
from uuid import UUID

import boto3

from config import settings
from lib.logger import logger
from ports.file_storage import FileStoragePort


class MinioStorageAdapter(FileStoragePort):
    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            endpoint_url=f"http://{settings.MINIO_ENDPOINT}",
            aws_access_key_id=settings.MINIO_ACCESS_KEY,
            aws_secret_access_key=settings.MINIO_SECRET_KEY,
        )
        self._ensure_bucket()

    def _ensure_bucket(self):
        buckets = self.s3.list_buckets()
        names = [b["Name"] for b in buckets.get("Buckets", [])]
        if settings.MINIO_BUCKET_NAME not in names:
            self.s3.create_bucket(Bucket=settings.MINIO_BUCKET_NAME)

    def save(self, document_id: UUID, filename: str, file_data: bytes) -> str:
        path = f"documents/{document_id}_{filename}"
        self.s3.put_object(Bucket=settings.MINIO_BUCKET_NAME, Key=path, Body=file_data)
        logger.success(f"File uploaded to MinIO: {path}")
        return path

    def generate_download_url(self, path: str, original_filename: str, expires: int = 900) -> str:
        disposition = f'attachment; filename="{quote(original_filename)}"'
        url = self.s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": settings.MINIO_BUCKET_NAME,
                "Key": path,
                "ResponseContentDisposition": disposition
            },
            ExpiresIn=expires
        )
        logger.debug(f"Generated download URL for {path}")
        return url