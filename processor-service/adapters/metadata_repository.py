from typing import Optional

from loguru import logger
from sqlalchemy import create_engine, MetaData, Table, update
from config import settings
from ports.metadata_repository import MetadataRepositoryInterface


class PostgresMetadataRepository(MetadataRepositoryInterface):
    def __init__(self) -> None:
        dsn = (
            f"postgresql+psycopg://{settings.postgres_user}:{settings.postgres_password}"
            f"@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
        )
        self.engine = create_engine(dsn)
        metadata = MetaData()
        self.table = Table("documents", metadata, autoload_with=self.engine)

    def update(self, document_id: str, text_preview: str, pages: Optional[int]) -> None:
        stmt = (
            update(self.table)
            .where(self.table.c.id == document_id)
            .values(text_preview=text_preview[:2000], pages=pages)
        )
        with self.engine.begin() as conn:
            conn.execute(stmt)
        logger.info("Metadata updated for {}", document_id)