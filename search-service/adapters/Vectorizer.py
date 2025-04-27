import asyncio
import os

from sentence_transformers import SentenceTransformer

from config import settings
from ports.Vectorizer import Vectorizer
from utils.logger import get_logger

logger = get_logger()


class LocalVectorizer(Vectorizer):
    def __init__(self) -> None:
        model_path = os.path.join("/models", settings.embedding_model_name.replace("/", "_"))
        logger.info("Initializing LocalVectorizer", model_name=settings.embedding_model_name, model_path=model_path)

        self.model = SentenceTransformer(model_path)

    async def vectorize(self, text: str) -> list[float]:
        logger.info("Vectorizing text", text_length=len(text))

        loop = asyncio.get_running_loop()
        embedding = await loop.run_in_executor(None, self.model.encode, text)
        return embedding.tolist()
