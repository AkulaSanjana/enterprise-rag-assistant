from dotenv import load_dotenv
load_dotenv()

from app.ingestion.document_loader import load_pdf
from app.ingestion.text_splitter import split_documents
from app.retrieval.vector_store import create_vector_store


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


# Step 4: Semantic search
question = "What is the vacation policy?"

results = vector_store.similarity_search(
    question,
    k=2
)

print("\n--- SEMANTIC SEARCH ---")
print(f"Question: {question}")

for index, result in enumerate(results, start=1):
    print(f"\n--- Result {index} ---")
    print(result.page_content)
    print("Metadata:", result.metadata)