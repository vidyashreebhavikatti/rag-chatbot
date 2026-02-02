
from fastapi import FastAPI, UploadFile
from services.pdf_loader import load_and_chunk_pdf
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "RAG Chatbot Backend Running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile):
    chunks = load_and_chunk_pdf(file.file)

    return {
        "status": "success",
        "total_chunks": len(chunks),
        "preview": chunks[:2]  # just for testing
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
