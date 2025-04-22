import logging

from fastapi import FastAPI, Depends

from adapters.kafka_producer import KafkaEventProducer
from adapters.minio_storage import MinioStorageAdapter
from delivery.handlers.upload import router as upload_router
from delivery.middlewares.error_handler import ExceptionLoggingMiddleware
from delivery.middlewares.request_logger import RequestLoggerMiddleware
from usecases.upload_document import UploadDocumentUseCase
from utils.logger import logger

logging.getLogger("uvicorn.access").disabled = True
logging.getLogger("uvicorn.error").disabled = True

app = FastAPI()

app.add_middleware(ExceptionLoggingMiddleware)
app.add_middleware(RequestLoggerMiddleware)

storage = MinioStorageAdapter()
kafka = KafkaEventProducer()
usecase = UploadDocumentUseCase(storage=storage, publisher=kafka)

app.state.upload_usecase = usecase

@app.on_event("startup")
async def startup():
    logger.info("Starting API service")
    await kafka.connect()

@app.on_event("shutdown")
async def shutdown():
    logger.info("Shutting down API service")
    await kafka.close()

app.include_router(upload_router, dependencies=[Depends(lambda: usecase)])
