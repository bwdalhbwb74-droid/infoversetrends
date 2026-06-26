import os
import json
import time
import threading
import requests
import feedparser
import schedule

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

# =====================================================
# CONFIG
# =====================================================

TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID", "YOUR_CHAT_ID")

TOPICS_FILE = "topics.json"
USED_FILE = "used_topics.json"

# =====================================================
# RSS FEEDS
# =====================================================

ARABIC_FEEDS = [
    "https://www.skynewsarabia.com/web/rss",
    "https://www.alarabiya.net/.mrss/ar.xml",
    "https://www.aljazeera.net/aljazeerarss/ar",
]

ENGLISH_FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://www.theverge.com/rss/index.xml",
]

# =====================================================
# FILE HELPERS
# =====================================================

def load_json(path, default):
    if not os.path.exists(path):
        return default

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return default


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_used_topics():
    return load_json(USED_FILE, [])


def save_used_topics(data):
    save_json(USED_FILE, data)


def load_topics():
    return load_json(TOPICS_FILE, [])


def save_topics(data):
    save_json(TOPICS_FILE, data)

# =====================================================
# RSS
# =====================================================

def get_feed_titles(url):
    try:
        feed = feedparser.parse(url)

        titles = []

        for entry in feed.entries:
            title = entry.title.strip()

            if title:
                titles.append(title)

        return titles

    except:
        return []

# =====================================================
# TOPICS
# =====================================================

def collect_topics():

    used = load_used_topics()

    collected = []

    # Arabic
    for feed in ARABIC_FEEDS:

        titles = get_feed_titles(feed)

        for title in titles:

            if title in used:
                continue

            if title in collected:
                continue

            collected.append(title)

            if len(collected) == 5:
                break

        if len(collected) == 5:
            break

    # English
    english = []

    for feed in ENGLISH_FEEDS:

        titles = get_feed_titles(feed)

        for title in titles:

            if title in used:
                continue

            if title in english:
                continue

            english.append(title)

            if len(english) == 5:
                break

        if len(english) == 5:
            break

    topics = collected + english

    save_topics(topics)

    return topics

# =====================================================
# TELEGRAM SEND
# =====================================================

def send_topics():
    topics = collect_topics()

    if len(topics) == 0:
        return

    message = "📋 مواضيع اليوم\n\n"

    for i, topic in enumerate(topics, start=1):
        message += f"{i}. {topic}\n"

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )
# =====================================================
# SCHEDULER
# =====================================================

def daily_job():
    print("Sending daily topics...")
    send_topics()


def scheduler_loop():

    schedule.every().day.at("05:00").do(daily_job)

    while True:
        schedule.run_pending()
        time.sleep(30)

# =====================================================
# TELEGRAM HANDLER
# =====================================================

async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message is None:
        return

    text = update.message.text.strip()

    if not text.isdigit():
        await update.message.reply_text(
            "أرسل رقمًا من 1 إلى 10."
        )
        return

    number = int(text)

    if number < 1 or number > 10:
        await update.message.reply_text(
            "أرسل رقمًا من 1 إلى 10."
        )
        return

    topics = load_topics()

    if len(topics) == 0:
        await update.message.reply_text(
            "لا توجد مواضيع حالياً."
        )
        return

    if number > len(topics):
        await update.message.reply_text(
            "هذا الرقم غير موجود."
        )
        return

    selected_topic = topics[number - 1]

    used = load_used_topics()

    if selected_topic not in used:
        used.append(selected_topic)
        save_used_topics(used)

    await update.message.reply_text(
        f"✅ الموضوع المختار:\n\n{selected_topic}"
    )

# =====================================================
# APPLICATION
# =====================================================

def build_app():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            receive_message
        )
    )

    return app
 # =====================================================
# MAIN
# =====================================================

def main():

    print("=" * 50)
    print("InfoVerse Publisher Started")
    print("=" * 50)

    # إرسال المواضيع مباشرة عند أول تشغيل (للاختبار)
    try:
        send_topics()
        print("Initial topics sent.")
    except Exception as e:
        print(f"Initial send failed: {e}")

    # تشغيل الجدولة في Thread مستقل
    scheduler_thread = threading.Thread(
        target=scheduler_loop,
        daemon=True
    )
    scheduler_thread.start()

    print("Scheduler started.")

    # تشغيل البوت
    app = build_app()

    print("Telegram bot started.")

    app.run_polling(
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()
