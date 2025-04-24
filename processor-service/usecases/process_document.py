from loguru import logger

from models.domain.document import DocumentTask


class ProcessDocumentUseCase:
    def __init__(self, storage, extractor, embedder, repo):
        self.storage = storage
        self.extractor = extractor
        self.embedder = embedder
        self.repo = repo

    def execute(self, task: DocumentTask):
        logger.info("Processing document: {}", task.document_id)

        file_bytes = self.storage.download(task.filepath)
        text = self.extractor.extract(file_bytes)
        embedding = self.embedder.encode(text)
        self.repo.save(task.document_id, embedding, text)

        logger.info("Document {} processed successfully", task.document_id)
