import requests
import feedparser

TOKEN = "8763023216:AAGTxJFJD2dnMtBHirSdx_fMhpyszuOkmS0"
CHAT_ID = "7330431242"

feeds = [
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://www.aljazeera.net/aljazeerarss/ar",
    "https://arabic.cnn.com/rss"
]

topics = []

for feed in feeds:
    try:
        data = feedparser.parse(feed)

        for item in data.entries[:10]:
            title = item.title.strip()

            if title not in topics:
                topics.append(title)

    except:
        pass

arabic = []
english = []

for topic in topics:
    if any('\u0600' <= c <= '\u06FF' for c in topic):
        arabic.append(topic)
    else:
        english.append(topic)

message = "🔥 الترندات اليومية\n\n"

message += "🇸🇦 5 مواضيع عربية:\n"
for i, t in enumerate(arabic[:5], 1):
    message += f"{i}- {t}\n"

message += "\n🌍 5 مواضيع إنجليزية:\n"
for i, t in enumerate(english[:5], 1):
    message += f"{i}- {t}\n"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Done")
