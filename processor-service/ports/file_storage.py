from abc import ABC, abstractmethod

class FileStorageInterface(ABC):
    @abstractmethod
    def download(self, path: str) -> bytes:
        raise NotImplementedError()
