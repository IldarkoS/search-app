from adapters.searcher_client import SearcherClient

from lib.logger import logger


class SearchDocumentsUseCase:
    def __init__(self, searcher_client: SearcherClient):
        self.searcher_client = searcher_client

    async def search(self, query: str) -> list[dict]:
        logger.info("Executing search use case", query_length=len(query))
        return await self.searcher_client.search(query)