import os
import threading
import re
from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Initialize Flask web server
app = Flask(__name__)

# Helper function to make text bold
def make_bold(text):
    escaped_text = re.sub(r"([_*()~`>#+\-=|{}.!])", r"\\\1", text)  # Escape reserved characters
    return f"*{escaped_text}*"

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Welcome message with bold text
    await context.bot.send_message(
        chat_id=chat_id,
        text=make_bold("🎉 Welcome to the 🤑 Casino Hack Bot 🎲"),
        parse_mode="MarkdownV2"
    )

    # First image message
    await context.bot.send_photo(
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
    
    # Hack selection buttons
    await context.bot.send_photo(
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

# Function to handle button interactions
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge button press

    # Hack data
    hack_data = {
        "sikkim_hack": { ... },  # Complete the data as shown in your original code
        "goa_hack": { ... },
        "diuwin_hack": { ... },
        "okwin_hack": { ... }
    }

    if query.data in hack_data:
        hack = hack_data[query.data]
        await query.message.reply_video(video=hack["video"], caption=hack["caption"], parse_mode="MarkdownV2")
        await query.message.reply_audio(audio=hack["audio"], caption=hack["audio_caption"], parse_mode="MarkdownV2")
        await query.message.reply_document(document=hack["apk"], caption=hack["apk_caption"], parse_mode="MarkdownV2")
        # Remaining hack buttons
        ...

# Webhook endpoint to handle updates from Telegram
@app.route(f'/webhook/<token>', methods=['POST'])
def webhook(token):
    if token == os.getenv("BOT_TOKEN"):  # Use environment variable for security
        json_data = request.get_json()
        bot = Bot(token=token)
        bot.process_new_updates([Update.de_json(json_data, bot)])
        return "OK", 200
    return "Unauthorized", 403

# Flask home endpoint
@app.route('/')
def home():
    return "Bot is running!"

# Run Flask server
def run_flask():
    port = int(os.environ.get("PORT", 8443))  # Use Render's dynamic port
    app.run(host='0.0.0.0', port=port)

# Run Telegram bot using webhook
def run_telegram_bot():
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # Store your bot token in Render environment variables
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Render app URL
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Set up webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=8443,  # Use HTTPS port
        url_path=BOT_TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{BOT_TOKEN}"
    )

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()  # Run Flask server in a thread
    run_telegram_bot()
