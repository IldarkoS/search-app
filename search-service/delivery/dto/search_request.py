from pydantic import BaseModel, Field

class SearchRequest(BaseModel):
    query: str = Field(..., description="Text fragment to search similar documents for")
