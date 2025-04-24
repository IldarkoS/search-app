from abc import ABC, abstractmethod

class VectorRepositoryInterface(ABC):
    @abstractmethod
    def save(self, document_id: str, embedding: list[float], text: str):
        raise NotImplementedError()
