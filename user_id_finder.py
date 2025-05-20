import nest_asyncio
nest_asyncio.apply()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# توکن ربات
TOKEN = "8116708167:AAHBAmCionn4V7EaL0kbSbU_iqvNrBnCmZs"
# آی‌دی عددی کاربر مجاز
AUTHORIZED_USER_ID = 99842418  # آی‌دی عددی واقعی را اینجا بگذار

# هندلر برای /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام.")

# هندلر پیام‌ها فقط از کاربر خاص
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id == AUTHORIZED_USER_ID:
        await update.message.reply_text("✅سلام به خودم")
    else:
        # اگر کاربر مجاز نباشد، واکنشی نشان داده نمی‌شود
        return

# تابع اصلی اجرا
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 ربات در حال اجراست...")
    await app.run_polling()

# اجرای درست با سازگاری nest_asyncio
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
