import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def discover_articles(base_url: str) -> list:
    try:
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[WARN] Failed to fetch {base_url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    domain = urlparse(base_url).netloc
    article_links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        full_url = urljoin(base_url, href)
        if domain in full_url and any(x in full_url for x in ["article", "news", "story"]):
            article_links.add(full_url)

    return list(article_links)