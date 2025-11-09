import re

def summarize_article(text: str, max_sentences: int = 3) -> str:
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    if not sentences:
        return ""
    summary = " ".join(sentences[:max_sentences])
    return summary