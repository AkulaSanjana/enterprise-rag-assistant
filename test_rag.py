from dotenv import load_dotenv

load_dotenv()

from app.ingestion.document_loader import load_pdf
from app.ingestion.text_splitter import split_documents
from app.retrieval.vector_store import create_vector_store
from app.generation.rag_chain import generate_answer


PDF_PATH = "data/sample_document.pdf"


# Step 1: Load PDF
documents = load_pdf(PDF_PATH)

print("\n--- DOCUMENT LOADING ---")
print(f"Pages loaded: {len(documents)}")


# Step 2: Split into chunks
chunks = split_documents(documents)

print("\n--- TEXT CHUNKING ---")
print(f"Total chunks created: {len(chunks)}")


# Step 3: Create vector store
vector_store = create_vector_store(chunks)

print("\n--- VECTOR STORE ---")
print("Vector store created successfully.")


# Step 4: Ask a question
question = "What is the remote work policy?"

print("\n--- QUESTION ---")
print(question)


# Step 5: Retrieve relevant chunks
retrieved_documents = vector_store.similarity_search(
    question,
    k=2
)

print("\n--- RETRIEVED DOCUMENTS ---")

for index, document in enumerate(retrieved_documents, start=1):
    print(f"\nResult {index}:")
    print(document.page_content[:500])


# Step 6: Generate final answer
answer = generate_answer(
    question,
    retrieved_documents
)

print("\n--- GENERATED ANSWER ---")
print(answer)

print("\n--- SOURCES ---")

for document in retrieved_documents:
    source = document.metadata.get("source", "Unknown")
    page = document.metadata.get("page", "Unknown")

    print(f"Source: {source}, Page: {page}")