from abc import ABC, abstractmethod

class Vectorizer(ABC):
    @abstractmethod
    async def vectorize(self, text: str) -> list[float]:
        raise NotImplementedError()