from functools import lru_cache

from adapters.embedding_model import EmbeddingModelAdapter
from adapters.metadata_repository import PostgresMetadataRepository
from adapters.minio_storage import MinioStorageAdapter
from adapters.text_extractor import TextExtractorAdapter
from adapters.vector_repository import VectorRepositoryAdapter
from usecases.process_document import ProcessDocumentUseCase


@lru_cache(maxsize=1)
def get_embedding_model() -> EmbeddingModelAdapter:
    return EmbeddingModelAdapter()


@lru_cache(maxsize=1)
def get_minio() -> MinioStorageAdapter:
    return MinioStorageAdapter()


@lru_cache(maxsize=1)
def get_vector_repo() -> VectorRepositoryAdapter:
    return VectorRepositoryAdapter()


@lru_cache(maxsize=1)
def get_text_extractor() -> TextExtractorAdapter:
    return TextExtractorAdapter()

@lru_cache(maxsize=1)
def get_metadata_repo():
    return PostgresMetadataRepository()

@lru_cache(maxsize=1)
def get_process_document_usecase() -> ProcessDocumentUseCase:
    return ProcessDocumentUseCase(
        storage=get_minio(),
        extractor=get_text_extractor(),
        embedder=get_embedding_model(),
        repo=get_vector_repo(),
        metadata_repo=get_metadata_repo(),
    )
