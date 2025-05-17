from abc import ABC, abstractmethod
from typing import Optional

class MetadataRepositoryInterface(ABC):
    @abstractmethod
    def update(
        self,
        document_id: str,
        preview_text: str,
        pages: Optional[int],
    ) -> None:
        ...