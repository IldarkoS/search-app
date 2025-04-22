from uuid import uuid4

from fastapi import UploadFile

from ports.event_publisher import EventPublisherPort
from ports.file_storage import FileStoragePort


class UploadDocumentUseCase:
    def __init__(self, storage: FileStoragePort, publisher: EventPublisherPort):
        self.storage = storage
        self.publisher = publisher

    async def execute(self, file: UploadFile) -> str:
        document_id = uuid4()
        file_data = await file.read()

        path = self.storage.save(document_id, file.filename, file_data)

        await self.publisher.publish("document_uploaded", {
            "document_id": str(document_id),
            "filename": file.filename,
            "filepath": path,
        })

        return document_id
