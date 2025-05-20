import nest_asyncio
nest_asyncio.apply()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TTOKEN = "8116708167:AAGpx-sO13KIPJzZLpl8MtutDf8bMnIK0PQ"

# دستور /start برای تست اولیه
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات هستم. هر پیامی بدی آی‌دی‌تو چاپ می‌کنم.")

# تابع گرفتن و چاپ آی‌دی کاربر
async def show_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_id = user.id
    username = user.username
    full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
    
    print(f"👤 کاربر جدید:")
    print(f"ID: {user_id}")
    print(f"Username: @{username}" if username else "Username: [نداره]")
    print(f"Full Name: {full_name}")
    
    await update.message.reply_text(f"آی‌دی عددی شما: `{user_id}`", parse_mode="Markdown")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, show_user_id))

    print("✅ ربات در حال اجراست...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
