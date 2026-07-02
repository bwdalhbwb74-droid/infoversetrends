"""
InfoVerse Hub V2
Telegram Bot
"""

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN
from topics import load_topics


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /start
    """

    await update.message.reply_text(
        "👋 أهلاً بك في InfoVerse Hub V2\n\n"
        "استخدم /topics لعرض مواضيع اليوم."
    )


async def topics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /topics
    """

    data = load_topics()

    if not data["topics"]:
        await update.message.reply_text(
            "❌ لا توجد مواضيع حالياً."
        )
        return

    message = "🔥 <b>مواضيع اليوم</b>\n\n"

    message += "━━━━━━━━━━━━━━\n\n"

    message += "🇸🇦 <b>المواضيع العربية</b>\n\n"

    arabic = []
    english = []

    for topic in data["topics"]:

        if topic.get("language") == "arabic":

            arabic.append(topic)

        else:

            english.append(topic)

    number = 1
    
    for topic in arabic:

        message += (
            f"{number}️⃣ {topic['category']}\n"
            f"📰 {topic['title']}\n\n"
        )

        number += 1

    message += "━━━━━━━━━━━━━━\n\n"

    message += "🌍 <b>المواضيع الإنجليزية</b>\n\n"

    for topic in english:

        message += (
            f"{number}️⃣ {topic['category']}\n"
            f"📰 {topic['title']}\n\n"
        )

        number += 1
        
    message += "━━━━━━━━━━━━━━\n\n"

    message += (
        "📩 <b>أرسل رقم الموضوع لبدء كتابة المقال.</b>"
    )

    await update.message.reply_text(
        message,
        parse_mode="HTML"
    )


async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle text messages.
    """

    text = update.message.text.strip()

    # إذا كانت الرسالة رقم
    if text.isdigit():

        data = load_topics()
        topics = data["topics"]

        index = int(text) - 1

        if index < 0 or index >= len(topics):
            await update.message.reply_text(
                "❌ رقم الموضوع غير صحيح."
            )
            return

        topic = topics[index]

        message = (
            f"📰 {topic['title']}\n\n"
            f"📂 التصنيف: {topic['category']}\n\n"
            f"📝 الملخص:\n{topic['summary']}\n\n"
            f"🔗 المصدر:\n{topic['link']}"
        )

        await update.message.reply_text(message)
        return

    # أي رسالة ليست رقم تعتبر مقالاً (سنضيف معالجتها لاحقاً)
    await update.message.reply_text(
        "✅ تم استلام المقال."
    )


def start_bot():
    """
    Start Telegram Bot.
    """

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("topics", topics))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            messages,
        )
    )

    print("✅ Telegram Bot Started.")

    app.run_polling()
