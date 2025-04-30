from adapters.searcher_client import SearcherClient

class SearchDocumentsUseCase:
    def __init__(self, searcher_client: SearcherClient):
        self.searcher_client = searcher_client

    async def search(self, query: str, top_k: int = 5) -> list[dict]:
        return await self.searcher_client.search(query, top_k)