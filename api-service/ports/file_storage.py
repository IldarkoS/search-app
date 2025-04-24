from abc import ABC, abstractmethod
from uuid import UUID

class FileStoragePort(ABC):
    @abstractmethod
    def save(self, document_id: UUID, filename: str, file_data: bytes) -> str:
        raise NotImplementedError()