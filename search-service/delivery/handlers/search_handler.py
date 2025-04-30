from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse

from delivery.dto.search_request import SearchRequest
from delivery.dto.search_response import SearchResponse
from lib.logger import get_logger

logger = get_logger()


def create_search_router() -> APIRouter:
    router = APIRouter()

    @router.post("/", response_model=SearchResponse)
    async def search_documents(request: Request, body: SearchRequest) -> SearchResponse:
        logger.info("Search request received", query=body.query)

        search_service = request.app.state.search_service
        try:
            results = await search_service.search_similar_documents(body.query)
            return SearchResponse(results=results)
        except Exception as e:
            logger.exception("Search failed", error=str(e))
            raise HTTPException(status_code=500, detail="Search failed")

    return router
