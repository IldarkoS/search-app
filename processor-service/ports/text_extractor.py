from abc import ABC, abstractmethod

class TextExtractorInterface(ABC):
    @abstractmethod
    def extract(self, file_bytes: bytes) -> str:
        raise NotImplementedError()