from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from adapters.SearcherRepository import QdrantSearcherRepository
from adapters.Vectorizer import LocalVectorizer
from config import settings
from delivery.handlers.search_handler import create_search_router
from lib.logger import init_logger, get_logger
from usecases.search_service import SearchService

logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_logger(settings.log_level)
    logger.info("Starting Search Service...")

    vectorizer = LocalVectorizer()
    searcher = QdrantSearcherRepository()
    search_service = SearchService(vectorizer, searcher)

    app.state.vectorizer = vectorizer
    app.state.searcher = searcher
    app.state.search_service = search_service

    logger.info("Search Service initialized successfully")
    yield
    logger.info("Shutting down Search Service...")


app = FastAPI(
    title="Searcher Service",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(
    create_search_router(),
    prefix="/search",
    tags=["search"]
)


@app.get("/health/", tags=["internal"])
async def health_check():
    return JSONResponse(content={"status": "ok"})
