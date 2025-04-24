from dataclasses import dataclass

@dataclass
class DocumentTask:
    document_id: str
    filename: str
    filepath: str
