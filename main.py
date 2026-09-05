from fastapi import FastAPI

app = FastAPI(
    title="Enterprise RAG Knowledge Assistant",
    description="API for an enterprise Retrieval-Augmented Generation system",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Enterprise RAG Knowledge Assistant is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }