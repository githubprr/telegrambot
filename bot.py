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
        caption="<b>Subscribe to my channel for updates!🔥</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✅SUBSCRIBE✅", url="https://t.me/+5icz2F7eIn0zZDI1")]])
    )

    # Hack selection buttons
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://sstournaments.com/piyush/image2.jpg",
        caption="Choose your preferred Color Prediction Master Hack!💸",
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
            "video": "https://file-to-link-nx-ccf8d5eda5c0.herokuapp.com/dl/6777ceb13aaf8bb8c01b0f8b",
            "caption": "Here is your SIKKIM VIP HACK video! 🎮",
            "audio": "https://sstournaments.com/piyush/sikkimaudio.mp3",
            "audio_caption": "<b>Listen to activate hack 🌟 Register: http://www.sikkim7.com/#/register?invitationCode=73728400111</b>"
        },
        "goa_hack": {
            "video": "https://file-to-link-nx-ccf8d5eda5c0.herokuapp.com/dl/6777cede3aaf8bb8c01b0f91",
            "caption": "Here is your GOA STAR HACK video! 🎮",
            "audio": "https://sstournaments.com/piyush/goahack.mp3",
            "audio_caption": "Listen to activate hack 🌟 Register: https://www.bing009.com/#/register?invitationCode=416623809168"
        },
        "diuwin_hack": {
            "video": "https://file-to-link-nx-ccf8d5eda5c0.herokuapp.com/dl/6777ce263aaf8bb8c01b0f86",
            "caption": "Here is your DIUWIN GRAND HACK video! 🎮",
            "audio": "https://sstournaments.com/piyush/diuwinhack.mp3",
            "audio_caption": "Listen to activate hack 🌟 Register: https://diuwinapp.pro/#/register?invitationCode=42677100202"
        },
        "okwin_hack": {
            "video": "https://sstournaments.com/piyush/okwinhack.mp4",
            "caption": "Here is your OKWIN SURE HACK video! 🎮",
            "audio": "https://sstournaments.com/piyush/okwinhack.mp3",
            "audio_caption": "Listen to activate hack 🌟 Register: https://www.okowin.com/#/register?invitationCode=282452739393"
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
    application = ApplicationBuilder().token("7446057407:AAFsS-f-_lPLgeXM5H7ox59oCofa8cniTGk").build()
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
