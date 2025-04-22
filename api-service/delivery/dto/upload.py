from typing import Literal
from uuid import UUID

from pydantic import BaseModel


class UploadResponse(BaseModel):
    document_id: UUID
    status: Literal["processing"]

class UploadRequest(BaseModel):
    document_id: str
    filename: str
    filepath: str