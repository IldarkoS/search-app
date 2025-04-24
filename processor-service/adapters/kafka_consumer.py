import json

from aiokafka import AIOKafkaConsumer
from loguru import logger

from config import settings
from models.domain.document import DocumentTask
from ports.event_consumer import EventConsumerInterface


class KafkaConsumerAdapter(EventConsumerInterface):
    def __init__(self):
        self._consumer = AIOKafkaConsumer(
            settings.kafka_topic,
            bootstrap_servers=settings.kafka_bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            group_id="processor-group"
        )

    async def start(self, callback):
        await self._consumer.start()
        logger.info("Kafka consumer started on topic '{}'", settings.kafka_topic)
        try:
            async for msg in self._consumer:
                logger.debug("Received raw Kafka message: {}", msg.value)
                try:
                    task = DocumentTask(**msg.value)
                    await callback(task)
                except Exception as e:
                    logger.exception("Failed to process message: {}", e)
        finally:
            await self._consumer.stop()
            logger.info("Kafka consumer stopped")
