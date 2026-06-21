import requests
import feedparser

TOKEN = "8763023216:AAGTxJFJD2dnMtBHirSdx_fMhpyszuOkmS0"
CHAT_ID = "7330431242"

feeds = {
    "عربي": "https://news.google.com/rss?hl=ar&gl=SA&ceid=SA:ar",
    "AI": "https://news.google.com/rss/search?q=AI&hl=en-US&gl=US&ceid=US:en",
    "Tech": "https://news.google.com/rss/search?q=Technology&hl=en-US&gl=US&ceid=US:en",
    "Gaming": "https://news.google.com/rss/search?q=Gaming&hl=en-US&gl=US&ceid=US:en",
    "Business": "https://news.google.com/rss/search?q=Business&hl=en-US&gl=US&ceid=US:en",
}

try:
    msg = "🔥 الترندات اليومية\n\n"

    # عربي
    ar = feedparser.parse(feeds["عربي"])
    msg += "🇸🇦 5 مواضيع عربية:\n"

    for i, item in enumerate(ar.entries[:5], 1):
        title = item.title.split(" - ")[0]
        msg += f"{i}- {title}\n"

    msg += "\n🌍 5 مواضيع إنجليزية:\n"

    english_topics = []

    for category in ["AI", "Tech", "Gaming", "Business"]:
        feed = feedparser.parse(feeds[category])

        if len(feed.entries) > 0:
            english_topics.append(feed.entries[0].title.split(" - ")[0])

    # نجيب موضوع إضافي من AI
    extra = feedparser.parse(feeds["AI"])

    if len(extra.entries) > 1:
        english_topics.append(extra.entries[1].title.split(" - ")[0])

    for i, topic in enumerate(english_topics[:5], 1):
        msg += f"{i}- {topic}\n"

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

    print("Trends sent successfully")

except Exception as e:
    print(e)
