import re

KEYWORDS = ["AI", "technology", "innovation", "science"]

def filter_articles(text: str) -> bool:
    if not text:
        return False
    for kw in KEYWORDS:
        if re.search(rf"\b{kw}\b", text, re.IGNORECASE):
            return True
    return False