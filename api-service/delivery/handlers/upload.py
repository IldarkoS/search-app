from fastapi import APIRouter, UploadFile, File, Request

from delivery.dto.upload import UploadResponse
from usecases.upload_document import UploadDocumentUseCase

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/", response_model=UploadResponse)
async def upload_document(
    request: Request,
    file: UploadFile = File(...)
):
    usecase: UploadDocumentUseCase = request.app.state.upload_usecase
    document_id = await usecase.execute(file)
    return UploadResponse(document_id=document_id, status="processing")