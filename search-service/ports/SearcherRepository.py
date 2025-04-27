from abc import ABC, abstractmethod


class SearcherRepository(ABC):
    @abstractmethod
    async def search(self, embedding: list[float], top_k: int) -> list[dict[str, float]]:
        raise NotImplementedError()