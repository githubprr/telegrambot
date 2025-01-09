# Required imports
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Initialize Flask web server
app = Flask(__name__)

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Welcome message
    await context.bot.send_message(chat_id=chat_id, text="Welcome to the 🤑 Casino Hack Bot 🎲")

    # First image message
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://drive.google.com/uc?id=19p7j4tb9vIz_Ff6vAbcA_cMgnQLasC0O",
        caption="Yeh mera main channel hai, jaha mein apna kaam dikhata hu. Mere channel ko subscribe kree, aur latest khabre prapt kree.🔥",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✅SUBSCRIBE✅", url="https://t.me/+5icz2F7eIn0zZDI1")]])
    )

    # Hack selection buttons
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://sstournaments.com/piyush/image2.jpg",
        caption="🛍 Apna Choice ke according Color Prediciton Master Hack choose karo.💸 Tumhare paas mauka hai profit wale VIP Hacks Ko Free Mai Lene Ka.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✅SIKKIM VIP HACK✅", callback_data="sikkim_hack")],
            [InlineKeyboardButton("✅GOA STAR HACK✅", callback_data="goa_hack")],
            [InlineKeyboardButton("✅DIUWIN GRAND HACK✅", callback_data="diuwin_hack")],
            [InlineKeyboardButton("✅OKWIN SURE HACK✅", callback_data="okwin_hack")]
        ])
    )

# Function to handle button interactions
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge button press

    # Video and audio responses based on button clicked
    hack_data = {
        "sikkim_hack": {
            "video": "BAACAgUAAxkBAAMJZ4AuXlxgQqMD85aOAyggbKVz6p0AAicVAAJSL5hX1q9yAbuNEt42BA",
            "caption": "Here is your SIKKIM VIP HACK video! 🎮"
        },
        "goa_hack": {
            "video": "BAACAgUAAxkBAAMDZ4AtCw6kcCEMNnw_iPxkF3cDhkkAAioVAAJSL5hXDOa_YxKmrOE2BA",
            "caption": "Here is your GOA STAR HACK video! 🎮"
        },
        "diuwin_hack": {
            "video": "BAACAgUAAxkBAAMVZ4AvAAFKugxu0xXzJWKyAgHRaK_YAAIlFQACUi-YV23guxciLQ0dNgQ",
            "caption": "Here is your DIUWIN GRAND HACK video! 🎮"
        },
        "okwin_hack": {
            "video": "BAACAgUAAxkBAAMTZ4Au9_kqCAT_0VoxjqwKVqtFcOAAAiwVAAJSL5hX62NsRnhGekY2BA",
            "caption": "Here is your OKWIN SURE HACK video! 🎮"
        }
    }

    if query.data in hack_data:
        hack = hack_data[query.data]
        await query.message.reply_video(video=hack["video"], caption=hack["caption"])
        await query.message.reply_audio(audio=hack["audio"], caption=hack["audio_caption"])

# Flask endpoints
@app.route('/')
def home():
    return "Bot is running!"

@app.route('/test')
def test():
    return "Test endpoint active!"

# Run Telegram bot
def run_telegram_bot():
    application = ApplicationBuilder().token("7446057407:AAFHB_sOytsxgRQA54ySLxGY9yIyraWvIlI").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.run_polling()

# Run Flask server
def run_flask():
    app.run(host='0.0.0.0', port=10000)

# Main entry point
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    run_telegram_bot()
