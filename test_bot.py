import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN") or "توکن_اینجا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات async هستم.")

async def run():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ ربات در حال اجراست...")
    await app.run_polling()

# بدون asyncio.run
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
