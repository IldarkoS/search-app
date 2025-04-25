import asyncio

from loguru import logger

from adapters.kafka_consumer import KafkaConsumerAdapter
from di import get_process_document_usecase


async def handle_task(task):
    logger.info("Handling document task: {}", task.document_id)
    get_process_document_usecase().execute(task)


def run_consumer():
    asyncio.run(KafkaConsumerAdapter().start(handle_task))
