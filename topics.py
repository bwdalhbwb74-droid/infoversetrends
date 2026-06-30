"""
InfoVerse Hub V2
Topics Manager
"""

import json

from rss import fetch_all_feeds
from filter import filter_articles
from ranking import get_top_articles


TOPICS_FILE = "topics.json"


def save_topics(topics):
    """
    Save topics to JSON.
    """

    with open(TOPICS_FILE, "w", encoding="utf-8") as file:

        json.dump(
            {
                "count": len(topics),
                "topics": topics
            },
            file,
            ensure_ascii=False,
            indent=4
        )


def load_topics():
    """
    Load topics from JSON.
    """

    try:

        with open(TOPICS_FILE, "r", encoding="utf-8") as file:

            return json.load(file)

    except FileNotFoundError:

        return {
            "count": 0,
            "topics": []
        }


def collect_topics():
    """
    Collect today's topics.
    """

    print("Fetching RSS feeds...")

    articles = fetch_all_feeds()

    print(f"Fetched {len(articles)} articles.")

    articles = filter_articles(articles)

    print(f"{len(articles)} articles after filtering.")

    topics = get_top_articles(articles, 10)

    save_topics(topics)

    print(f"Saved {len(topics)} topics.")

    return topics
