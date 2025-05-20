import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN") or "توکن_را_اینجا_بگذار"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات async هستم.")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ ربات در حال اجراست...")
    await app.run_polling()

# اجرای درست بدون گیر افتادن در event loop error
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        # اگر حلقه‌ای در حال اجراست یا وجود ندارد
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
