from abc import ABC, abstractmethod

class EventPublisherPort(ABC):
    @abstractmethod
    async def publish(self, topic: str, event: dict) -> None:
        raise NotImplementedError()