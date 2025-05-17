from uuid import UUID

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Request

from delivery.dto.search import SearchRequest, SearchResponse, DocumentDetailResponse
from lib.logger import logger
from lib.text_extractor import extract_text
from usecases.search_document import SearchDocumentsUseCase

router = APIRouter()

def get_search_usecase(request: Request) -> SearchDocumentsUseCase:
    return request.app.state.search_usecase

@router.post("/", response_model=SearchResponse)
async def search_documents(
    request: Request,
    file: UploadFile = File(None),
    request_model: SearchRequest = Depends(),
    usecase: SearchDocumentsUseCase = Depends(get_search_usecase)
):
    if not file and not request_model.query:
        raise HTTPException(status_code=400, detail="Either file or query must be provided.")

    try:
        if file:
            file_data = await file.read()
            query = extract_text(file_data, file.filename)
        else:
            query = request_model.query
    except Exception as e:
        logger.error("Failed to extract text", error=str(e))
        raise HTTPException(status_code=400, detail="Failed to extract text from file.")

    total, results = await usecase.search(query=query, db=request.app.state.db)
    return SearchResponse(total=total, results=results)



@router.get("/{document_id}", response_model=DocumentDetailResponse)
async def get_document(document_id: UUID, request: Request):
    usecase: SearchDocumentsUseCase = request.app.state.search_usecase
    try:
        result = await usecase.get_by_id(document_id, db=request.app.state.db)
        return DocumentDetailResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
