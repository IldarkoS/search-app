from abc import ABC, abstractmethod


class SearcherRepository(ABC):
    @abstractmethod
    async def search(self, embedding: list[float]) -> list[dict[str, float]]:
        raise NotImplementedError()