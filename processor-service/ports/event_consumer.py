from abc import ABC, abstractmethod

from models.domain.document import DocumentTask


class EventConsumerInterface(ABC):
    @abstractmethod
    async def start(self, callback: callable):
        raise NotImplementedError()