from pathlib import Path
from uuid import uuid4, UUID

from fastapi import UploadFile

from lib.logger import logger
from ports.event_publisher import EventPublisherPort
from ports.file_storage import FileStoragePort


class UploadDocumentUseCase:
    def __init__(self, storage: FileStoragePort, publisher: EventPublisherPort):
        self._storage = storage
        self._publisher = publisher

    async def upload(self, file: UploadFile, db) -> UUID:
        document_id = uuid4()
        logger.info("Uploading file", document_id=str(document_id), filename=file.filename)

        file_data = await file.read()

        file_path = self._storage.save(document_id, file.filename, file_data)
        logger.info("File saved to MinIO", path=file_path)

        title = Path(file.filename).stem
        doc_type = Path(file.filename).suffix.lstrip(".")
        await db.execute(
            "INSERT INTO documents(id,title,type,file_path) VALUES($1,$2,$3,$4)",
            document_id, title, doc_type, file_path,
        )
        logger.info("Metadata saved to PSQL", path=file_path)

        await self._publisher.publish(
            event={
                "document_id": str(document_id),
                "filename": file.filename,
                "filepath": file_path,
            }
        )
        logger.info("Upload event published", topic="uploaded-documents")

        return document_id
