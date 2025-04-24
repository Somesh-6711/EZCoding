# backend/app/api/routes.py

from typing import Optional
from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
import aiofiles

from app.core.language_detection import detect_language
from app.core.utils import split_code_into_chunks
from app.models.code_explainer import explain_code_logic

router = APIRouter()

class ExplainRequest(BaseModel):
    code: Optional[str] = None
    filename: Optional[str] = None

@router.post("/health")
async def health_check():
    return {"status": "API is healthy!"}

@router.post("/detect_language")
async def detect_code_language(req: ExplainRequest):
    if not req.code:
        raise HTTPException(status_code=400, detail="`code` is required")
    lang = detect_language(req.code, req.filename)
    return {"language": lang}

@router.post("/explain_code")
async def explain_code_endpoint(
    code: Optional[str] = None,
    filename: Optional[str] = None,
    file: UploadFile = File(None),
):
    """
    Accept either JSON {code, filename} or a multipart file upload.
    Returns language + aggregated explanation.
    """
    # 1) Read from file if provided
    if file:
        contents = await file.read()
        code = contents.decode("utf-8")
        filename = file.filename

    if not code:
        raise HTTPException(status_code=400, detail="No code or file provided.")

    # 2) Detect language
    lang = detect_language(code, filename)

    # 3) Split into chunks (if large) and explain each
    chunks = split_code_into_chunks(code)
    explanations = [explain_code_logic(chunk, lang) for chunk in chunks]
    full_explanation = "\n\n".join(explanations)

    return {"language": lang, "explanation": full_explanation}
