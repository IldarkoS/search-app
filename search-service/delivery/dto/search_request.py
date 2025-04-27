from pydantic import BaseModel, Field

class SearchRequest(BaseModel):
    query: str = Field(..., description="Text fragment to search similar documents for")
    top_k: int = Field(default=5, description="Number of most similar documents to return")
