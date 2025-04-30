from typing import Any

from qdrant_client import QdrantClient
from qdrant_client.http.models import SearchRequest, Filter

from config import settings
from lib.logger import get_logger
from ports.SearcherRepository import SearcherRepository

logger = get_logger()


class QdrantSearcherRepository(SearcherRepository):
    def __init__(self) -> None:
        logger.info("Initializing QdrantSearcherRepository",
                    host=settings.qdrant_host, port=settings.qdrant_port)

        self.client = QdrantClient(
            host=settings.qdrant_host,
            port=settings.qdrant_port,
        )

    async def search(self, embedding: list[float]) -> list[dict[str, Any]]:
        logger.info("Searching in Qdrant with threshold filtering", threshold=0.3)

        hits = self.client.search(
            collection_name=settings.qdrant_collection,
            query_vector=embedding,
            limit=100,
            with_payload=False,
        )

        filtered = [
            {"document_id": hit.id, "score": hit.score}
            for hit in hits
            if hit.score >= 0.3
        ]

        logger.info("Filtered results", total=len(hits), returned=len(filtered))

        return filtered
