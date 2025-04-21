from fastapi import FastAPI
from routers import upload
from services.kafka_producer import init_kafka_producer, close_kafka_producer
from utils.logger import logger

app = FastAPI()
app.include_router(upload.router)

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting api-service")
    await init_kafka_producer()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info(f"Shutting down api-service")
    await close_kafka_producer()
