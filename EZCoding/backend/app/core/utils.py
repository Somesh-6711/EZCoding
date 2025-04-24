from typing import List

def split_code_into_chunks(code: str, max_lines: int = 50) -> List[str]:
    """
    Splits code into chunks of up to max_lines each.
    """
    lines = code.splitlines()
    return ["\n".join(lines[i : i + max_lines]) for i in range(0, len(lines), max_lines)]
