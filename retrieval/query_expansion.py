from generation.llm import generate_answer

def expand_query(query):
    prompt = f"""
Generate 3 different search queries related to the user query.

User Query:
{query}

Instructions:
- Each query should have a different perspective
- Keep them short and useful for retrieval

Return as a list.
"""

    response = generate_answer(prompt)

    queries = [q.strip("- ").strip() for q in response.split("\n") if q.strip()]

    return queries