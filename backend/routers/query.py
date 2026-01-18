from fastapi import APIRouter

router = APIRouter()

@router.post("/query")
def query_rag(question: str):
    return {
        "question": question,
        "answer": "This is a dummy answer from RAG"
    }
