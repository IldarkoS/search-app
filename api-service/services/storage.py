import boto3
from uuid import UUID
from config import settings

s3 = boto3.client(
    "s3",
    endpoint_url=f"http://{settings.MINIO_ENDPOINT}",
    aws_access_key_id=settings.MINIO_ACCESS_KEY,
    aws_secret_access_key=settings.MINIO_SECRET_KEY,
)

def ensure_bucket_exists():
    buckets = s3.list_buckets()
    bucket_names = [b["Name"] for b in buckets.get("Buckets", [])]
    if settings.MINIO_BUCKET_NAME not in bucket_names:
        s3.create_bucket(Bucket=settings.MINIO_BUCKET_NAME)

def upload_file_to_minio(document_id: UUID, file_data: bytes, filename: str) -> str:
    ensure_bucket_exists()
    path = f"documents/{document_id}_{filename}"
    s3.put_object(Bucket=settings.MINIO_BUCKET_NAME, Key=path, Body=file_data)
    return path
