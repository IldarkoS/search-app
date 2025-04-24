from abc import ABC, abstractmethod

class EmbeddingModelInterface(ABC):
    @abstractmethod
    def encode(self, text: str) -> list[float]:
        raise NotImplementedError()
