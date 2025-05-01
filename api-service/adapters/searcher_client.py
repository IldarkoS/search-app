import httpx
from loguru import logger

from config import settings
from ports.searcher_client import SearcherClientInterface


class SearcherClient(SearcherClientInterface):
    def __init__(self):
        self.base_url = settings.SEARCHER_SERVICE_URL
        logger.info(f"Searcher service url: {self.base_url}/search/")

    async def search(self, query: str) -> list[dict]:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/search/",
                json={
                    "query": query,
                },
                timeout=10,
            )
            response.raise_for_status()

            return response.json()["results"]
