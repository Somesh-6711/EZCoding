import os
import torch
from functools import lru_cache
from transformers import pipeline

# Try to import the new OpenAI client
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

@lru_cache()
def get_summarizer():
    device = 0 if torch.cuda.is_available() else -1
    return pipeline("summarization", model="Salesforce/codet5-base", device=device)

def explain_code_logic(code: str, language: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and OpenAI is not None:
        # Initialize the new client
        client = OpenAI(api_key=api_key)
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert programming tutor."},
                {
                    "role": "user",
                    "content": (
                        f"Please explain this {language} code step by step, line by line:\n\n{code}"
                    ),
                },
            ],
            temperature=0.0,
            max_tokens=512,
        )
        return resp.choices[0].message.content.strip()

    # Fallback to local summarizer
    summarizer = get_summarizer()
    summary = summarizer(
        code,
        max_length=256,
        min_length=64,
        num_beams=5,
        early_stopping=True,
    )
    return summary[0]["summary_text"].strip()
