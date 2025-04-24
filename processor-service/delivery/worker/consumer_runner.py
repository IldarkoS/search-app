import asyncio
from loguru import logger
from adapters.kafka_consumer import KafkaConsumerAdapter
from usecases.process_document import ProcessDocumentUseCase

from adapters.minio_storage import MinioStorageAdapter
from adapters.text_extractor import TextExtractorAdapter
from adapters.embedding_model import EmbeddingModelAdapter
from adapters.vector_repository import VectorRepositoryAdapter


async def handle_task(task):
    logger.info("Handling document task: {}", task.document_id)
    usecase = ProcessDocumentUseCase(
        MinioStorageAdapter(),
        TextExtractorAdapter(),
        EmbeddingModelAdapter(),
        VectorRepositoryAdapter(),
    )
    usecase.execute(task)


def run_consumer():
    consumer = KafkaConsumerAdapter()
    asyncio.run(consumer.start(handle_task))
