import io

from docx import Document as DocxDocument
from loguru import logger
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams


def extract_text(file_content: bytes, filename: str) -> str:
    if filename.endswith(".txt"):
        return file_content.decode("utf-8")

    elif filename.endswith(".pdf"):
        logger.debug("Detected .pdf file")
        with io.BytesIO(file_content) as f:
            output = io.StringIO()
            extract_text_to_fp(f, output, laparams=LAParams(), output_type='text', codec=None)
            return output.getvalue()

        return "\n".join(page.extract_text() or "" for page in reader.pages)

    elif filename.endswith(".docx"):
        logger.debug("Detected .docx file")
        with io.BytesIO(file_content) as f:
            doc = DocxDocument(f)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text

    else:
        raise ValueError("Unsupported file type")
