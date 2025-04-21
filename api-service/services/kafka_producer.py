import asyncio
import json
from aiokafka import AIOKafkaProducer
from config import settings

from utils.logger import logger

producer = None

async def init_kafka_producer():
    global producer
    producer = AIOKafkaProducer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    for attempt in range(10):
        try:
            await producer.start()
            logger.success("Connected to Kafka")
            return
        except Exception as e:
            logger.warning(f"Kafka not ready (attempt {attempt + 1}/10): {e}")
            await asyncio.sleep(3)

    logger.critical("Could not connect to Kafka after retries")
    raise ConnectionError("Kafka not available")

async def send_upload_event(event: dict):
    await producer.send_and_wait("document_uploaded", event)

async def close_kafka_producer():
    global producer
    if producer:
        await producer.stop()
