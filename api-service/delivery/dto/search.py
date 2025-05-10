from pydantic import BaseModel, Field
from typing import Optional, List

class SearchRequest(BaseModel):
    query: Optional[str] = Field(None, description="Text fragment to search similar documents for")

class SearchItem(BaseModel):
    document_id: str
    score: float
    title: str | None = None
    type: str | None = None
    pages: int | None = None
    thumb_url: str | None = None

class SearchResponse(BaseModel):
    total: int
    results: list[SearchItem]