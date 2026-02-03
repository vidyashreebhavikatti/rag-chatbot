import pdfplumber
from typing import List

def extract_text_from_pdf(file) -> str:
    """
    Extracts text from a PDF file object.
    """
    full_text = ""

    with pdfplumber.open(file) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:
                full_text += text + "\n"

    return full_text


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100
) -> List[str]:
    """
    Splits text into overlapping chunks.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

    return chunks


def load_and_chunk_pdf(file) -> List[str]:
    """
    Full pipeline:
    PDF -> text -> chunks
    """
    text = extract_text_from_pdf(file)
    return chunk_text(text)


