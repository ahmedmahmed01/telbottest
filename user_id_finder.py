import nest_asyncio
nest_asyncio.apply()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8116708167:AAHBAmCionn4V7EaL0kbSbU_iqvNrBnCmZs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام!نصیری هستم.")

# پاسخ به هر پیام متنی با آی‌دی کاربر
async def show_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_id = user.id
    await update.message.reply_text(f"🆔 آی‌دی عددی شما: `{user_id}`", parse_mode="Markdown")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, show_user_id))

    print("✅ ربات در حال اجراست...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
