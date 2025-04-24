import io

from docx import Document as DocxDocument
from loguru import logger
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

from ports.text_extractor import TextExtractorInterface


class TextExtractorAdapter(TextExtractorInterface):
    MIN_TEXT_LENGTH = 100

    def extract(self, file_bytes: bytes) -> str:
        logger.info("Extracting text from file...")

        if file_bytes.startswith(b"%PDF"):
            text = self._extract_pdf(file_bytes)
        elif file_bytes.startswith(b"PK"):
            text = self._extract_docx(file_bytes)
        else:
            text = self._extract_txt(file_bytes)

        length = len(text)
        logger.info("Extracted {} characters", length)

        if length < self.MIN_TEXT_LENGTH:
            logger.warning("Text too short ({} characters). Document may be empty or corrupted.", length)

        return text

    def _extract_txt(self, file_bytes: bytes) -> str:
        logger.debug("Detected .txt file")
        return file_bytes.decode("utf-8", errors="ignore")

    def _extract_docx(self, file_bytes: bytes) -> str:
        logger.debug("Detected .docx file")
        with io.BytesIO(file_bytes) as f:
            doc = DocxDocument(f)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text

    def _extract_pdf(self, file_bytes: bytes) -> str:
        logger.debug("Detected .pdf file")
        with io.BytesIO(file_bytes) as f:
            output = io.StringIO()
            extract_text_to_fp(f, output, laparams=LAParams(), output_type='text', codec=None)
            return output.getvalue()
