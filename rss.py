"""
InfoVerse Hub V2
RSS Reader
"""

import json
import feedparser
import re
from html import unescape

RSS_FILE = "rss_sources.json"


def load_sources():
    """
    Load RSS sources from JSON file.
    """

    with open(RSS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def clean_html(text):
    """
    Remove HTML tags from RSS content.
    """

    if not text:
        return ""

    text = unescape(text)

    text = re.sub(r"<[^>]+>", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()

def fetch_feed(url):
    """
    Fetch one RSS feed.
    """

    feed = feedparser.parse(url)

    articles = []

    for item in feed.entries:

        articles.append({
            "title": clean_html(item.get("title", "")),
            "summary": clean_html(item.get("summary", "")),
            "link": item.get("link", "").strip(),
            "published": item.get("published", "").strip(),
        })

    return articles


def fetch_all_feeds():
    """
    Fetch all RSS feeds.
    """

    sources = load_sources()

    all_articles = []

    for language, categories in sources.items():

        for category, feeds in categories.items():

            for url in feeds:

                try:

                    articles = fetch_feed(url)

                    for article in articles:

                        article["language"] = language
                        article["category"] = category

                        all_articles.append(article)

                except Exception as error:

                    print(f"RSS Error: {url}")
                    print(error)

    return all_articles
