import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("8792695521:AAEq0qyTQSDUj-r-Nmt3G1fEZkMY_KGmDYQ")

WEB_URL = "https://invite-earn-bot.onrender.com"

async def start(update, context):

    keyboard = [
        [InlineKeyboardButton(
            "🚀 Start Earning",
            web_app=WebAppInfo(url=WEB_URL)
        )]
    ]

    await update.message.reply_photo(
        photo="https://i.imgur.com/7QFQK9R.png",
        caption="📢 Welcome to Invite & Earn Money\n\nClick Start to open earning panel",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
