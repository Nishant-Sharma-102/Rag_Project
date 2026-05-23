from groq import Groq
from core.config import GROQ_API_KEY, LLM_MODEL, MAX_TOKENS, TEMPERATURE

client = Groq(api_key="")

def generate_answer(prompt):
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    return response.choices[0].message.content