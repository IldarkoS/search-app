from loguru import logger
from sentence_transformers import SentenceTransformer

from ports.embedding_encoder import EmbeddingModelInterface


class EmbeddingModelAdapter(EmbeddingModelInterface):
    def __init__(self):
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
        logger.info("Loading embedding model: {}", model_name)
        self.model = SentenceTransformer(model_name)
        logger.info("Model loaded successfully")

    def encode(self, text: str) -> list[float]:
        if not text or not text.strip():
            raise ValueError("Cannot encode empty text")

        logger.debug("Encoding text of length: {}", len(text))

        embedding = self.model.encode(text, normalize_embeddings=True)
        vector = embedding.tolist()

        logger.info("Generated embedding of dimension {}", len(vector))
        return vector
