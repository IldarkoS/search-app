from uuid import UUID

from fastapi import APIRouter, UploadFile, File, Request, HTTPException
from delivery.dto.upload import UploadResponse
from usecases.upload_document import UploadDocumentUseCase
from lib.logger import logger

router = APIRouter()

@router.post("/", response_model=UploadResponse)
async def upload_document(
    request: Request,
    file: UploadFile = File(...)
) -> UploadResponse:
    usecase: UploadDocumentUseCase = request.app.state.upload_usecase

    logger.info("Upload request received", filename=file.filename)

    try:
        document_id: UUID = await usecase.upload(file)
        logger.info("Upload successful", document_id=str(document_id))
        return UploadResponse(document_id=document_id, status="processing")
    except Exception as e:
        logger.exception("Upload failed", error=str(e))
        raise HTTPException(status_code=500, detail="Failed to upload document")
