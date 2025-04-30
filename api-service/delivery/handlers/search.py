from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends, Request
from usecases.search_document import SearchDocumentsUseCase

from delivery.dto.search import SearchResponse
from lib.logger import logger
from lib.text_extractor import extract_text

router = APIRouter()

@router.post("/", response_model=SearchResponse)
async def search_documents(
    request: Request,
    file: UploadFile = File(None),
    text: str = Form(None),
    top_k: int = Form(5),
):
    usecase: SearchDocumentsUseCase = request.app.state.search_usecase
    if not file and not text:
        raise HTTPException(status_code=400, detail="Either file or text must be provided.")

    if file:
        try:
            content = await file.read()
            text = extract_text(content, file.filename)
        except Exception as e:
            logger.error("Failed to extract text", error=str(e))
            raise HTTPException(status_code=400, detail="Failed to extract text from file.")

    results = await usecase.search(text, top_k)
    return SearchResponse(results=results)
