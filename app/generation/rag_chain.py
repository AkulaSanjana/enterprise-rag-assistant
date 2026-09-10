from langchain_openai import ChatOpenAI


def generate_answer(question, documents):
    """
    Generate an answer using only the retrieved document context.
    """

    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    prompt = f"""
You are an enterprise knowledge assistant.

Answer the user's question using only the context below.

If the answer is not available in the context, say:
"I do not have enough information in the provided documents."

Keep the answer clear and concise.

Context:
{context}

Question:
{question}

Answer:
"""

    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    response = model.invoke(prompt)

    return response.content