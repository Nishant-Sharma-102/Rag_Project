def build_prompt(query, retrieved_docs):
    context = "\n\n".join(
        [f"[Source {i+1}]: {doc.page_content}" for i, doc in enumerate(retrieved_docs)]
    )

    prompt = f"""
You are an AI assistant. Answer ONLY from the provided context.

Context:
{context}

Question:
{query}

Instructions:
- Answer in clear bullet points
- Cite sources like (Source 1), (Source 2)
- If answer is not in context, say: "I don't know"
- Do NOT make up information
- Keep answer concise and structured
"""

    return prompt