from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.language_detection import detect_language
from app.models.code_explainer import explain_code_logic

router = APIRouter()

# … your existing /health and /detect_language endpoints …

class ExplainRequest(BaseModel):
    code: str
    filename: Optional[str] = None

@router.post("/explain_code")
async def explain_code_endpoint(req: ExplainRequest):
    """
    POST /explain_code
    {
      "code": "...",
      "filename": "example.py"   # optional
    }
    Returns:
    {
      "language": "python",
      "explanation": "Step-by-step explanation..."
    }
    """
    try:
        lang = detect_language(req.code, req.filename)
        explanation = explain_code_logic(req.code, lang)
        return {"language": lang, "explanation": explanation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
