import os
import re
import threading
from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler

# Initialize Flask app
app = Flask(__name__)

# Helper function to make text bold
def make_bold(text):
    escaped_text = re.sub(r"([_*()~`>#+\-=|{}.!])", r"\\\1", text)  # Escape reserved characters
    return f"*{escaped_text}*"

# Telegram bot handlers
def start(update: Update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text=make_bold("🎉 Welcome to the 🤑 Casino Hack Bot 🎲"),
        parse_mode="MarkdownV2"
    )

    context.bot.send_photo(
        chat_id=chat_id,
        photo="https://drive.google.com/uc?id=19p7j4tb9vIz_Ff6vAbcA_cMgnQLasC0O",
        caption=make_bold(
            "🔥 Yeh mera main channel hai, jaha mein apna kaam dikhata hu. "
            "Mere channel ko subscribe kree, aur latest khabre prapt kree! 🔥"
        ),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✅SUBSCRIBE✅", url="https://t.me/+5icz2F7eIn0zZDI1")]]
        ),
        parse_mode="MarkdownV2"
    )

    context.bot.send_photo(
        chat_id=chat_id,
        photo="https://sstournaments.com/piyush/image2.jpg",
        caption=make_bold(
            "💥 Apne Choice ke according Color Prediction Master Hack choose karo 💸\n\n"
            "💎 Tumhare paas mauka hai Profit wale VIP Hacks Ko Free Mai Lene Ka 💎"
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✅SIKKIM VIP HACK✅", callback_data="sikkim_hack")],
            [InlineKeyboardButton("✅GOA STAR HACK✅", callback_data="goa_hack")],
            [InlineKeyboardButton("✅DIUWIN GRAND HACK✅", callback_data="diuwin_hack")],
            [InlineKeyboardButton("✅OKWIN SURE HACK✅", callback_data="okwin_hack")]
        ]),
        parse_mode="MarkdownV2"
    )

def button_handler(update: Update, context):
    query = update.callback_query
    query.answer()

    # Data for different hacks
    hack_data = {
        "sikkim_hack": {
            "video": "BAACAgUAAxkBAAIFQ2eAOe5opaSq7JJdWVqrLC-X0LEOAAIsFQACUi-YV2dFPleZscusNgQ",
            "audio": "CQACAgUAAxkBAAIFSWeAOiQz7gvpHAWOjqCJM0HobBtqAAKaEgACmJEAAVR7IngSjkXofTYE",
            "apk": "BQACAgUAAxkBAAIFUWeAOmX_kgABXmwrS5tReBEf1zPKawACohIAApiRAAFUDlhg__DwTCs2BA",
            "name": "🔥 SIKKIM VIP HACK 🔥",
            "caption": make_bold("🚀 Here is your SIKKIM VIP HACK video! 🎮"),
        },
        # Define other hacks similarly...
    }

    if query.data in hack_data:
        hack = hack_data[query.data]
        context.bot.send_video(chat_id=query.message.chat_id, video=hack["video"], caption=hack["caption"], parse_mode="MarkdownV2")
        context.bot.send_audio(chat_id=query.message.chat_id, audio=hack["audio"])
        context.bot.send_document(chat_id=query.message.chat_id, document=hack["apk"])

# Flask route for Telegram webhook
@app.route(f'/{os.getenv("BOT_TOKEN")}', methods=['POST'])
def webhook():
    json_data = request.get_json()
    update = Update.de_json(json_data, bot)
    dispatcher.process_update(update)
    return "OK", 200

# Main function to set up webhook
if __name__ == "__main__":
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # Ensure this is set in the environment variables
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # e.g., "https://your-app-name.onrender.com"

    # Initialize Telegram bot
    bot = Bot(token=BOT_TOKEN)

    # Set webhook
    bot.set_webhook(url=f"{WEBHOOK_URL}/{BOT_TOKEN}")

    # Set up Dispatcher
    dispatcher = Dispatcher(bot, None)
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))

    # Start Flask server
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
