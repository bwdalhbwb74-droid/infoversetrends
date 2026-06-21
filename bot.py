import requests
import feedparser

TOKEN = "8763023216:AAGTxJFJD2dnMtBHirSdx_fMhpyszuOkmS0"
CHAT_ID = "7330431242"

try:
    arabic_feeds = [
        "https://arabic.cnn.com/rss",
        "https://www.aljazeera.net/aljazeerarss/ar",
    ]

    english_feeds = [
        "https://feeds.bbci.co.uk/news/rss.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    ]

    arabic_topics = []
    english_topics = []

    for feed in arabic_feeds:
        data = feedparser.parse(feed)
        for entry in data.entries[:5]:
            title = entry.title.strip()
            if title not in arabic_topics:
                arabic_topics.append(title)

    for feed in english_feeds:
        data = feedparser.parse(feed)
        for entry in data.entries[:5]:
            title = entry.title.strip()
            if title not in english_topics:
                english_topics.append(title)

    arabic_topics = arabic_topics[:5]
    english_topics = english_topics[:5]

    message = "🔥 الترندات اليومية\n\n"

    message += "🇸🇦 5 مواضيع عربية:\n"
    for i, topic in enumerate(arabic_topics, 1):
        message += f"{i}- {topic}\n"

    message += "\n🌍 5 مواضيع إنجليزية:\n"
    for i, topic in enumerate(english_topics, 1):
        message += f"{i}- {topic}\n"

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    print("Topics sent successfully")

except Exception as e:
    print(e)
