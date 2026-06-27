import feedparser
import re


# ==========================================
# TEXT HELPERS
# ==========================================

def clean_text(text):

    if not text:
        return ""

    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")

    return " ".join(text.split())
# ==========================================
# RSS PROVIDER
# ==========================================

def fetch_rss(feed_url, limit=20):

    news = []

    try:

        feed = feedparser.parse(feed_url)

        if getattr(feed, "bozo", False):
            return []

        for entry in feed.entries[:limit]:

            title = clean_text(
                entry.get("title", "")
            )

            if not title:
                continue

            summary = clean_text(
                entry.get("summary", "")
                or entry.get("description", "")
            )

            news.append({

                "title": title,

                "summary": summary,

                "link": entry.get(
                    "link",
                    ""
                ),

                "published": entry.get(
                    "published",
                    ""
                ),

                "source": feed_url,

                "provider": "rss"

            })

    except Exception as e:

        print(e)

    return news
    # ==========================================
# FETCH CATEGORY RSS
# ==========================================

def fetch_category(feeds, limit_per_feed=20):

    all_news = []

    for feed in feeds:

        news = fetch_rss(
            feed,
            limit_per_feed
        )

        all_news.extend(news)

    return all_news


# ==========================================
# FETCH ALL RSS
# ==========================================

def fetch_all_categories(rss_sources):

    data = {
        "arabic": {},
        "english": {}
    }

    # Arabic
    for category, feeds in rss_sources["arabic"].items():

        data["arabic"][category] = fetch_category(feeds)

    # English
    for category, feeds in rss_sources["english"].items():

        data["english"][category] = fetch_category(feeds)

    return data
