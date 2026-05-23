from generation.llm import generate_answer

def rewrite_query(query):
    prompt = f"""
Rewrite the user query to make it more clear, specific, and optimized for document search.

Original Query:
{query}

Rewritten Query:
"""

    rewritten = generate_answer(prompt)
    return rewritten.strip()