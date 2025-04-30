from pydantic import BaseModel, Field
from typing import Optional, List

class SearchResult(BaseModel):
    document_id: str
    score: float

class SearchResponse(BaseModel):
    results: List[SearchResult]

class SearchRequest(BaseModel):
    query: Optional[str] = Field(None, description="Text fragment to search similar documents for")
    top_k: int = Field(default=5, description="Number of most similar documents to return")