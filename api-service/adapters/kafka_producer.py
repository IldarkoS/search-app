import asyncio
import json
from aiokafka import AIOKafkaProducer
from ports.event_publisher import EventPublisherPort
from config import settings
from utils.logger import logger

class KafkaEventProducer(EventPublisherPort):
    def __init__(self):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    async def connect(self):
        for attempt in range(10):
            try:
                await self.producer.start()
                logger.success("Connected to Kafka")
                return
            except Exception as e:
                logger.warning(f"Kafka not ready (attempt {attempt + 1}/10): {e}")
                await asyncio.sleep(3)
        logger.critical("Could not connect to Kafka after retries")
        raise ConnectionError("Kafka not available")

    async def publish(self, topic: str, event: dict) -> None:
        await self.producer.send_and_wait(topic, event)

    async def close(self):
        await self.producer.stop()
