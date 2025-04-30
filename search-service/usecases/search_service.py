from ports.SearcherRepository import SearcherRepository
from ports.Vectorizer import Vectorizer
from lib.logger import get_logger

logger = get_logger()

class SearchService:
    def __init__(self, vectorizer: Vectorizer, searcher: SearcherRepository) -> None:
        self.vectorizer = vectorizer
        self.searcher = searcher

    async def search_similar_documents(self, query: str, top_k: int = 5) -> list[dict]:
        logger.info("Starting search for similar documents", query_length=len(query), top_k=top_k)

        embedding = await self.vectorizer.vectorize(query)
        logger.info("Vectorization completed")

        results = await self.searcher.search(embedding, top_k)
        logger.info("Search completed", results_count=len(results))

        return results
