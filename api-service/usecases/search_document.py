from adapters.minio_storage import MinioStorageAdapter
from adapters.searcher_client import SearcherClient

from lib.logger import logger


class SearchDocumentsUseCase:
    def __init__(self, searcher_client: SearcherClient, storage: MinioStorageAdapter):
        self.searcher_client = searcher_client
        self.storage = storage

    async def search(self, query: str, db, limit=20, offset=0) -> list[dict]:
        logger.info("Executing search use case", query_length=len(query))
        raw = await self.searcher_client.search(query)

        ids = [r["document_id"] for r in raw[offset:offset + limit]]
        scores = {r["document_id"]: r["score"] for r in raw}

        rows = await db.fetch(
            "SELECT id,title,type,pages FROM documents WHERE id = ANY($1)", ids
        )
        meta = {str(r["id"]): r for r in rows}

        enriched = []
        for _id in ids:
            m = meta.get(_id, {})
            enriched.append({
                "document_id": _id,
                "score": scores[_id],
                "title": m.get("title"),
                "type": m.get("type"),
                "pages": m.get("pages"),
                "thumb_url": self.storage.presign_get(f"documents/{_id}_thumb.png")
                if m else None,
            })
        return len(raw), enriched