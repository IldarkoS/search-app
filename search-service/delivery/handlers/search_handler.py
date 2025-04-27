from fastapi import APIRouter, HTTPException

from delivery.dto.search_request import SearchRequest
from delivery.dto.search_response import SearchResponse
from usecases.search_service import SearchService
from utils.logger import get_logger

logger = get_logger()

def create_search_router(search_service: SearchService) -> APIRouter:
    router = APIRouter()

    @router.post("/", response_model=SearchResponse)
    async def search_documents(request: SearchRequest):
        logger.info("Received search request", query=request.query, top_k=request.top_k)

        try:
            results = await search_service.search_similar_documents(request.query, request.top_k)
            return SearchResponse(results=results)
        except Exception as e:
            logger.error("Search failed", error=str(e))
            raise HTTPException(status_code=500, detail="Internal server error")

    return router
