import nest_asyncio
nest_asyncio.apply()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8087765766:AAHZP3brmuQn_L2fh42Iypm_AEtEDEEfKCM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من یک ربات هستم.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ ربات در حال اجراست...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
