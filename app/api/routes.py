from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv

from app.ingestion.document_loader import load_pdf
from app.ingestion.text_splitter import split_documents
from app.retrieval.vector_store import create_vector_store
from app.generation.rag_chain import generate_answer


load_dotenv()

router = APIRouter()

PDF_PATH = "data/sample_document.pdf"


class ChatRequest(BaseModel):
    question: str


documents = load_pdf(PDF_PATH)
chunks = split_documents(documents)
vector_store = create_vector_store(chunks)


@router.post("/chat")
def chat(request: ChatRequest):

    retrieved_documents = vector_store.similarity_search(
        request.question,
        k=2
    )

    answer = generate_answer(
        request.question,
        retrieved_documents
    )

    sources = []

    for document in retrieved_documents:
        sources.append(
            {
                "source": document.metadata.get("source", "Unknown"),
                "page": document.metadata.get("page", "Unknown")
            }
        )

    return {
        "question": request.question,
        "answer": answer,
        "sources": sources
    }