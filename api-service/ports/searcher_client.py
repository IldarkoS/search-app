from abc import ABC, abstractmethod

class SearcherClientInterface(ABC):
    @abstractmethod
    def search(self, query: str) -> list[dict]:
        raise NotImplementedError()