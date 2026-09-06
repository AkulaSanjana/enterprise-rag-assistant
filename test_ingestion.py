from app.ingestion.document_loader import load_pdf
from app.ingestion.text_splitter import split_documents


PDF_PATH = "data/sample_document.pdf"


# Load the PDF
documents = load_pdf(PDF_PATH)

print("\n--- DOCUMENT LOADING ---")
print(f"Pages loaded: {len(documents)}")

if documents:
    print("\nFirst page metadata:")
    print(documents[0].metadata)

    print("\nFirst 300 characters:")
    print(documents[0].page_content[:300])


# Split the document into chunks
chunks = split_documents(documents)

print("\n--- TEXT CHUNKING ---")
print(f"Total chunks created: {len(chunks)}")

for index, chunk in enumerate(chunks[:3], start=1):
    print(f"\n--- Chunk {index} ---")
    print(chunk.page_content[:500])
    print("Metadata:", chunk.metadata)