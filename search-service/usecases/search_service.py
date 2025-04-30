from ports.SearcherRepository import SearcherRepository
from ports.Vectorizer import Vectorizer
from lib.logger import get_logger

logger = get_logger()

class SearchService:
    def __init__(self, vectorizer: Vectorizer, searcher: SearcherRepository) -> None:
        self.vectorizer = vectorizer
        self.searcher = searcher

    async def search_similar_documents(self, query: str) -> list[dict[str, float]]:
        logger.info("Starting semantic search", query_length=len(query))

        embedding = await self.vectorizer.vectorize(query)
        logger.info("Text vectorized", embedding_dim=len(embedding))

        results = await self.searcher.search(embedding)
        logger.info("Search finished", results_count=len(results))

        return results
