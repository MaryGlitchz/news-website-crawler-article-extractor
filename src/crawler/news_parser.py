import requests
from bs4 import BeautifulSoup
from datetime import datetime

def parse_article(url: str) -> dict:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "Untitled"
    paragraphs = [p.get_text() for p in soup.find_all("p")]
    text = "\n".join(paragraphs)
    authors = ", ".join([a.get_text() for a in soup.find_all(["span", "a"], {"class": ["author", "byline"]})]) or "Unknown"
    publish_date = datetime.utcnow().isoformat()
    top_image = soup.find("img")["src"] if soup.find("img") else ""

    return {
        "articleURL": url,
        "articleTitle": title.strip(),
        "articleText": text.strip(),
        "articleAuthors": authors.strip(),
        "articlePublishDate": publish_date,
        "articleWordCount": len(text.split()),
        "articleKeywords": "",
        "articleSummary": "",
        "articleTopImage": top_image
    }