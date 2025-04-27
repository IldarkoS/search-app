from qdrant_client import QdrantClient

from config import settings
from ports.SearcherRepository import SearcherRepository
from utils.logger import get_logger

logger = get_logger()

class QdrantSearcherRepository(SearcherRepository):
    def __init__(self) -> None:
        logger.info("Initializing QdrantSearcherRepository",
                    host=settings.qdrant_host, port=settings.qdrant_port)

        self.client = QdrantClient(
            host=settings.qdrant_host,
            port=settings.qdrant_port,
        )

    async def search(self, embedding: list[float], top_k: int) -> list[dict]:
        logger.info("Searching in Qdrant", top_k=top_k)

        hits = self.client.search(
            collection_name=settings.qdrant_collection,
            query_vector=embedding,
            limit=top_k,
        )

        return [
            {"document_id": hit.id, "score": hit.score}
            for hit in hits
        ]
