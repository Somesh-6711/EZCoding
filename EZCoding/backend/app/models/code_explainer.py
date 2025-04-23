import os
import torch
from functools import lru_cache
from transformers import pipeline

try:
    import openai
except ImportError:
    openai = None

@lru_cache()
def get_summarizer():
    device = 0 if torch.cuda.is_available() else -1
    return pipeline(
        "summarization",
        model="Salesforce/codet5-base",
        device=device,
    )

def explain_code_logic(code: str, language: str) -> str:
    """
    If OPENAI_API_KEY is set, use OpenAI's ChatCompletion for high-quality explanations.
    Otherwise fallback to the HF summarization pipeline.
    """
    # 1) If we have an OpenAI key, call the API
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and openai is not None:
        openai.api_key = api_key
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert programming tutor."},
                {
                    "role": "user",
                    "content": (
                        f"Please explain the following {language} code step by step, "
                        "in simple terms, line by line:\n\n"
                        f"{code}"
                    ),
                },
            ],
            max_tokens=512,
            temperature=0.0,
        )
        return resp.choices[0].message.content.strip()

    # 2) Otherwise fallback to HF summarization
    summarizer = get_summarizer()
    summary = summarizer(
        code,
        max_length=256,
        min_length=64,
        num_beams=5,
        early_stopping=True,
    )
    return summary[0]["summary_text"].strip()
