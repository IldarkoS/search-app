from fastapi import FastAPI

from adapters.SearcherRepository import QdrantSearcherRepository
from adapters.Vectorizer import LocalVectorizer
from config import settings
from delivery.handlers.search_handler import create_search_router
from usecases.search_service import SearchService
from lib.logger import init_logger

init_logger(settings.log_level)

app = FastAPI(title="Searcher Service")

vectorizer = LocalVectorizer()
searcher = QdrantSearcherRepository()
search_service = SearchService(vectorizer, searcher)

app.include_router(create_search_router(search_service), prefix="/search", tags=["search"])
