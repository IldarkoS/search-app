from pydantic import BaseModel
from uuid import UUID
from typing import Literal

class UploadResponse(BaseModel):
    document_id: UUID
    status: Literal["processing"]

class UploadEvent(BaseModel):
    document_id: str
    filename: str
    filepath: str
