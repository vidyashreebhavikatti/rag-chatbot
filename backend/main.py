from fastapi import FastAPI, UploadFile
import pdfplumber
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "RAG Chatbot Backend Running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile):
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return {"status": "success", "text_length": len(text)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)