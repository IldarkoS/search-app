import os
from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from adapters.kafka_producer import KafkaEventProducer
from adapters.minio_storage import MinioStorageAdapter
from adapters.searcher_client import SearcherClient
from delivery.handlers.search import router as search_router
from delivery.handlers.upload import router as upload_router
from delivery.middlewares.error_handler import ExceptionLoggingMiddleware
from delivery.middlewares.request_logger import RequestLoggerMiddleware
from lib.logger import logger
from usecases.search_document import SearchDocumentsUseCase
from usecases.upload_document import UploadDocumentUseCase


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting API service...")

    kafka = KafkaEventProducer()
    await kafka.connect()
    storage = MinioStorageAdapter()
    searcher_client = SearcherClient()

    upload_usecase = UploadDocumentUseCase(storage=storage, publisher=kafka)
    search_usecase = SearchDocumentsUseCase(searcher_client=searcher_client,
                                            storage=storage)

    db = await asyncpg.create_pool(dsn=os.getenv("PG_DSN"))

    app.state.db = db
    app.state.kafka = kafka
    app.state.upload_usecase = upload_usecase
    app.state.search_usecase = search_usecase

    logger.info("API service initialized successfully.")
    yield

    logger.info("Shutting down API service...")
    await kafka.close()
    await db.close()
    logger.info("API service shut down successfully.")

origins = [
    "http://localhost:5174",
    "http://localhost:5173",
]

app = FastAPI(
    title="API Gateway Service",
    version="1.0.0",
    description="Handles document uploads and search requests",
    lifespan=lifespan
)

app.add_middleware(ExceptionLoggingMiddleware)
app.add_middleware(RequestLoggerMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(upload_router, prefix="/upload", tags=["upload"])


@app.get("/health/", tags=["internal"])
async def health_check():
    return JSONResponse(content={"status": "ok"})
