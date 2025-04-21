from fastapi import APIRouter, UploadFile, File
from uuid import uuid4
from models.schema import UploadResponse, UploadEvent
from services.storage import upload_file_to_minio
from services.kafka_producer import send_upload_event
import asyncio

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    document_id = uuid4()
    file_data = await file.read()

    filepath = upload_file_to_minio(document_id, file_data, file.filename)

    event = UploadEvent(
        document_id=str(document_id),
        filename=file.filename,
        filepath=filepath
    )
    asyncio.create_task(send_upload_event(event.dict()))
    return UploadResponse(document_id=document_id, status="processing")
