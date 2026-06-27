import json

from config import (
    TOPICS_FILE,
    USED_TOPICS_FILE,
)

from storage import (
    load_json,
    save_json,
)

from providers import (
    clean_text,
    is_arabic,
    is_english,
    fetch_category,
)

# ==========================================
# LOAD RSS SOURCES
# ==========================================

with open("rss_sources.json", "r", encoding="utf-8") as f:
    RSS_SOURCES = json.load(f)


# ==========================================
# STORAGE
# ==========================================

def load_used_topics():
    return load_json(USED_TOPICS_FILE, [])


def save_used_topics(data):
    save_json(USED_TOPICS_FILE, data[-300:])


def load_topics():

    return load_json(
        TOPICS_FILE,
        {
            "date": "",
            "today": [],
            "history": []
        }
    )


def save_topics(data):

    save_json(TOPICS_FILE, data)


# ==========================================
# TITLE HELPERS
# ==========================================

def normalize_title(title):

    return clean_text(title).lower()


# ==========================================
# SCORE
# ==========================================

GOOD_WORDS = [

    "ai",
    "gpt",
    "openai",
    "google",
    "apple",
    "microsoft",
    "tesla",
    "samsung",

    "ذكاء",
    "جوجل",
    "آبل",
    "سامسونج",
    "تحديث",
    "إطلاق",
    "رسمي",
    "جديد"

]


def calculate_score(item):

    score = 0

    title = item["title"]
    summary = item["summary"]

    if 40 <= len(title) <= 90:
        score += 25

    if len(summary) >= 120:
        score += 20

    if any(c.isdigit() for c in title):
        score += 10

    if item["link"]:
        score += 5

    title_lower = title.lower()

    for word in GOOD_WORDS:

        if word.lower() in title_lower:
            score += 10

    return score
  # ==========================================
# FILTER NEWS
# ==========================================

def filter_news(news, used_topics, language):

    filtered = []

    seen = set()

    used = {
        normalize_title(title)
        for title in used_topics
    }

    for item in news:

        title = clean_text(item.get("title", ""))

        if not title:
            continue

        if language == "ar":

            if not is_arabic(title):
                continue

        else:

            if not is_english(title):
                continue

        normalized = normalize_title(title)

        if normalized in seen:
            continue

        if normalized in used:
            continue

        seen.add(normalized)

        if len(title) < 25:
            continue

        item["title"] = title
        item["summary"] = clean_text(
            item.get("summary", "")
        )

        item["score"] = calculate_score(item)

        filtered.append(item)

    filtered.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return filtered


# ==========================================
# SELECT BEST TOPIC
# ==========================================

def get_best_topic(category_name, feeds, used_topics, language):

    all_news = fetch_category(
        feeds,
        language
    )

    filtered = filter_news(
        all_news,
        used_topics,
        language
    )

    if not filtered:

        return {
            "category": category_name,
            "title": "لا يوجد موضوع مناسب اليوم",
            "summary": "",
            "link": "",
            "published": "",
            "source": "",
            "score": 0,
            "number": 0,
            "language": language
        }

    best = filtered[0]

    return {
        "category": category_name,
        "title": best["title"],
        "summary": best["summary"],
        "link": best["link"],
        "published": best["published"],
        "source": best["source"],
        "score": best["score"],
        "number": 0,
        "language": language
    }
# ==========================================
# BUILD TODAY TOPICS
# ==========================================

def build_today_topics():

    used_topics = load_used_topics()

    topics = []

    number = 1

    # Arabic
    for category, feeds in RSS_SOURCES["arabic"].items():

        topic = get_best_topic(
            category_name=category,
            feeds=feeds,
            used_topics=used_topics,
            language="ar"
        )

        topic["number"] = number

        topics.append(topic)

        if topic["title"] != "لا يوجد موضوع مناسب اليوم":
            used_topics.append(topic["title"])

        number += 1

    # English
    for category, feeds in RSS_SOURCES["english"].items():

        topic = get_best_topic(
            category_name=category,
            feeds=feeds,
            used_topics=used_topics,
            language="en"
        )

        topic["number"] = number

        topics.append(topic)

        if topic["title"] != "لا يوجد موضوع مناسب اليوم":
            used_topics.append(topic["title"])

        number += 1

    save_used_topics(used_topics)

    data = load_topics()

    data["date"] = ""
    data["today"] = topics

    if "history" not in data:
        data["history"] = []

    data["history"].extend(topics)

    save_topics(data)

    return topics
    # ==========================================
# BUILD TELEGRAM MESSAGE
# ==========================================

def build_telegram_message(topics):

    message = "🔥 مواضيع اليوم\n\n"

    message += "🇸🇦 المواضيع العربية\n\n"

    for topic in topics:

        if topic["language"] != "ar":
            continue

        message += (
            f"{topic['number']}. {topic['category']}\n"
            f"📰 {topic['title']}\n"
            f"⭐ Score: {topic['score']}\n\n"
        )

    message += "🌍 المواضيع الإنجليزية\n\n"

    for topic in topics:

        if topic["language"] != "en":
            continue

        message += (
            f"{topic['number']}. {topic['category']}\n"
            f"📰 {topic['title']}\n"
            f"⭐ Score: {topic['score']}\n\n"
        )

    message += (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "✍️ أرسل رقم الموضوع (1-11) لكتابة المقال."
    )

    return message


# ==========================================
# PUBLIC FUNCTION
# ==========================================

def generate_daily_topics():

    topics = build_today_topics()

    message = build_telegram_message(topics)

    return topics, message
