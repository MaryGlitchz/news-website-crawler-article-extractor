import json
import os
from datetime import datetime
from crawler.article_discovery import discover_articles
from crawler.news_parser import parse_article
from crawler.ai_summary import summarize_article
from utils.keyword_filter import filter_articles
from utils.language_detector import detect_language
from exporters.json_exporter import export_to_json
from exporters.csv_exporter import export_to_csv
from exporters.xml_exporter import export_to_xml

def main():
    input_file = os.path.join("data", "input_sites.txt")
    output_file = os.path.join("data", "output_sample.json")
    log_dir = os.path.join("data", "logs")
    os.makedirs(log_dir, exist_ok=True)

    with open(input_file, "r", encoding="utf-8") as f:
        sites = [line.strip() for line in f if line.strip()]

    all_articles = []
    for site in sites:
        print(f"[INFO] Discovering articles from {site}")
        urls = discover_articles(site)
        for url in urls:
            try:
                article_data = parse_article(url)
                article_data["articleLanguage"] = detect_language(article_data["articleText"])
                article_data["articleSummary"] = summarize_article(article_data["articleText"])
                article_data["meetsSearchCriteria"] = filter_articles(article_data["articleText"])
                article_data["scrapeSuccess"] = True
                article_data["scrapedAt"] = datetime.utcnow().isoformat()
                all_articles.append(article_data)
            except Exception as e:
                print(f"[ERROR] Failed to scrape {url}: {e}")

    export_to_json(all_articles, output_file)
    export_to_csv(all_articles, os.path.join("data", "articles.csv"))
    export_to_xml(all_articles, os.path.join("data", "articles.xml"))
    print(f"[INFO] Export complete. Total articles: {len(all_articles)}")

if __name__ == "__main__":
    main()