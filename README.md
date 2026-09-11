# Enterprise RAG Knowledge Assistant

A production-oriented Retrieval-Augmented Generation (RAG) application for querying enterprise documents using Large Language Models and semantic search.

## Overview

The goal of this project is to build a scalable enterprise knowledge assistant that can retrieve relevant information from company documents and generate grounded answers with source citations.

## Planned Features

- PDF document ingestion
- Intelligent text chunking
- Vector embeddings
- Semantic search and retrieval
- LLM-powered question answering
- Source citations
- LangGraph workflow orchestration
- RAG evaluation
- FastAPI backend
- Docker support
- Automated testing

## Tech Stack

- Python
- FastAPI
- LangChain
- LangGraph
- ChromaDB
- OpenAI
- Docker
- Pytest

## Architecture

Documents → Chunking → Embeddings → Vector Database → Retrieval → LLM → Answer + Sources

## Current Progress

### Day 1
- Initialized GitHub repository
- Created Python virtual environment
- Set up project structure
- Installed initial dependencies
- Created FastAPI application
- Added root and health-check endpoints
- Verified API using Swagger UI

## Running Locally

Activate the virtual environment:

```bash
source venv/bin/activate 
```

### Day 2

- Added PDF document ingestion using PyPDFLoader
- Added PDF file validation
- Implemented recursive text chunking
- Added configurable chunk size and overlap
- Preserved document metadata for future source citations
- Tested document loading and chunk generation

### Day 3

- Added OpenAI embeddings for document chunks
- Implemented ChromaDB vector storage
- Added persistent local vector database
- Implemented semantic similarity search
- Added environment variable support for API keys
- Tested end-to-end vector retrieval

### Day 4

- Built the end-to-end RAG question-answering pipeline
- Connected semantic retrieval to an OpenAI chat model
- Added context-grounded answer generation
- Added fallback behavior when information is missing
- Added basic source metadata to generated responses
- Tested retrieval and generation using enterprise policy questions

### Day 5

- Added FastAPI chat endpoint for RAG queries
- Connected semantic retrieval to API requests
- Added structured request validation using Pydantic
- Returned generated answers with source metadata
- Tested the RAG system through Swagger UI