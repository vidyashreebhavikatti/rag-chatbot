from fastapi import APIRouter, UploadFile
from services.pdf_loader import extract_text_from_pdf

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile):
    text = extract_text_from_pdf(file)
    return {
        "status": "success",
        "characters_extracted": len(text)
    }
