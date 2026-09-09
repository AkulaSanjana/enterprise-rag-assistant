from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


PERSIST_DIRECTORY = "chroma_db"


def create_vector_store(documents):
    """
    Create a Chroma vector store from document chunks.
    """

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )

    return vector_store


def load_vector_store():
    """
    Load an existing Chroma vector store.
    """

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    return Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )