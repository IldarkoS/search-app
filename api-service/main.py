from fastapi import FastAPI
from loguru import logger
import logging

from middleware.error_handler import ExceptionLoggingMiddleware
from middleware.request_logger import RequestLoggerMiddleware
from routers import upload
from services.kafka_producer import init_kafka_producer, close_kafka_producer
from utils.logger import logger


logging.getLogger("uvicorn.access").disabled = True
logging.getLogger("uvicorn.error").disabled = True
logging.getLogger("fastapi").disabled = True

app = FastAPI()

app.add_middleware(ExceptionLoggingMiddleware)
app.add_middleware(RequestLoggerMiddleware)

app.include_router(upload.router)

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting api-service")
    await init_kafka_producer()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info(f"Shutting down api-service")
    await close_kafka_producer()
