# file: backend/app/core/language_detection.py
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.util import ClassNotFound
from typing import Optional

def detect_language(code: str, filename: Optional[str] = None) -> str:
    """
    Try filename-based detection first; then fallback to pure code detection.
    Returns the first alias (e.g. "python"), or "text" if Pygments can't match.
    """
    try:
        if filename:
            lexer = guess_lexer_for_filename(filename, code)
        else:
            lexer = guess_lexer(code)
        # pick the first alias if available
        alias = lexer.aliases[0] if lexer.aliases else lexer.name.lower()
        return alias.lower()
    except ClassNotFound:
        return "text"
