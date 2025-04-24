from loguru import logger
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

from config import settings
from ports.vector_repository import VectorRepositoryInterface


class VectorRepositoryAdapter(VectorRepositoryInterface):
    def __init__(self):
        self.client = QdrantClient(
            host=settings.qdrant_host,
            port=settings.qdrant_port,
        )

        self.collection = settings.qdrant_collection

        existing = self.client.get_collections().collections
        if not any(col.name == self.collection for col in existing):
            logger.info("Creating Qdrant collection '{}'", self.collection)
            self.client.recreate_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=384, distance=Distance.COSINE)
            )
        else:
            logger.info("Qdrant collection '{}' already exists", self.collection)

    def save(self, document_id: str, embedding: list[float], text: str):
        logger.info("Saving document '{}' to Qdrant...", document_id)

        self.client.upsert(
            collection_name=self.collection,
            points=[
                PointStruct(
                    id=document_id,
                    vector=embedding,
                    payload={
                        "text": text
                    }
                )
            ]
        )

        logger.info("Document '{}' saved successfully to Qdrant", document_id)
