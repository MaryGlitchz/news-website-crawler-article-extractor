from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0

def detect_language(text: str) -> str:
    try:
        return detect(text) if text.strip() else "unknown"
    except Exception:
        return "unknown"