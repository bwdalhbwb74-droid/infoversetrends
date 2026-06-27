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
# LANGUAGE DETECTION
# ==========================================

def is_arabic(text):

    for c in text:
        if "\u0600" <= c <= "\u06FF":
            return True

    return False


def is_english(text):

    letters = 0
    english = 0

    for c in text:

        if c.isalpha():

            letters += 1

            if "a" <= c.lower() <= "z":
                english += 1

    if letters == 0:
        return False

    return (english / letters) >= 0.6
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

            item = {

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

            }

            news.append(item)

    except Exception as e:

        print(f"RSS ERROR: {feed_url}")
        print(e)

    return news
    # ==========================================
# FETCH CATEGORY
# ==========================================

def fetch_category(feeds, language, limit_per_feed=20):

    all_news = []

    for feed in feeds:

        news = fetch_rss(
            feed,
            limit_per_feed
        )

        for item in news:

            title = item["title"]

            if language == "ar":

                if not is_arabic(title):
                    continue

            else:

                if not is_english(title):
                    continue

            all_news.append(item)

    return all_news


# ==========================================
# FETCH ALL CATEGORIES
# ==========================================

def fetch_all_categories(rss_sources):

    data = {
        "arabic": {},
        "english": {}
    }

    for category, feeds in rss_sources["arabic"].items():

        data["arabic"][category] = fetch_category(
            feeds,
            "ar"
        )

    for category, feeds in rss_sources["english"].items():

        data["english"][category] = fetch_category(
            feeds,
            "en"
        )

    return data
