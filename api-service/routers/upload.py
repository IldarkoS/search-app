from fastapi import APIRouter, UploadFile, File
from uuid import uuid4
from models.schema import UploadResponse, UploadEvent
from services.storage import upload_file_to_minio
from services.kafka_producer import send_upload_event
import asyncio

from utils.logger import logger

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    document_id = uuid4()
    file_data = await file.read()

    logger.info(f"Received file upload: {file.filename} (size: {len(file_data)} bytes)")

    filepath = upload_file_to_minio(document_id, file_data, file.filename)

    event = UploadEvent(
        document_id=str(document_id),
        filename=file.filename,
        filepath=filepath
    )

    logger.debug(f"Sending event to Kafka: {event}")
    asyncio.create_task(send_upload_event(event.dict()))
    logger.success(f"Document accepted: {document_id}")

    return UploadResponse(document_id=document_id, status="processing")
