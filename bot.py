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

    await update.message.reply_text(
        "👋 أهلاً بك في InfoVerse Hub V2"
    )


async def topics(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = load_topics()

    if not data["topics"]:

        await update.message.reply_text(
            "لا توجد مواضيع حالياً."
        )

        return

    message = "📰 مواضيع اليوم\n\n"

    for index, topic in enumerate(data["topics"], start=1):

        message += f"{index}. {topic['title']}\n"

    await update.message.reply_text(message)


async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.strip()

    await update.message.reply_text(
        f"تم استلام:\n{text}"
    )


def start_bot():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(CommandHandler("topics", topics))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            messages
        )
    )

    print("Telegram Bot Started.")

    app.run_polling()
