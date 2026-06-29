"""
InfoVerse Hub V2
Topics Collector
"""

import json


def collect_topics():
    """
    Collect today's topics.
    """

    print("Collecting topics...")

    topics = []

    # TODO:
    # Read RSS sources
    # Fetch articles
    # Remove duplicates
    # Rank topics
    # Select top 10

    save_topics(topics)

    return topics


def save_topics(topics):
    """
    Save topics into topics.json
    """

    with open("topics.json", "w", encoding="utf-8") as file:
        json.dump(
            {
                "count": len(topics),
                "topics": topics
            },
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"{len(topics)} topics saved.")
