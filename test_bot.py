import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات هستم و روی Render اجرا می‌شم.")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 ربات در حال اجراست...")
    await app.run_polling()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        # در صورتی که event loop قبلاً فعال بوده
        if str(e).startswith("Cannot close a running event loop"):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
        else:
            raise
