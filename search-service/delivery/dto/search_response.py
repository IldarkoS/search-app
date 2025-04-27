from pydantic import BaseModel
from typing import List

class SearchResult(BaseModel):
    document_id: str
    score: float

class SearchResponse(BaseModel):
    results: List[SearchResult]
