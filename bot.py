# Required imports
import re
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Initialize Flask web server
app = Flask(__name__)

# Helper function to make text bold
def make_bold(text):
    escaped_text = re.sub(r"([_*\[\]()~`>#+\-=|{}.!])", r"\\\1", text)  # Escape reserved characters
    return f"*{escaped_text}*"

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Welcome message with bold text
    await context.bot.send_message(
        chat_id=chat_id,
        text=make_bold("Welcome to the 🤑 Casino Hack Bot 🎲"),
        parse_mode="MarkdownV2"
    )

    # First image message
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://drive.google.com/uc?id=19p7j4tb9vIz_Ff6vAbcA_cMgnQLasC0O",
        caption=make_bold(
            "Yeh mera main channel hai, jaha mein hamne bahut sare logo ka loss recover karwaya hai ."
            "Mere channel ko subscribe kree, Number Prediction + Big Small Sab Milegaa Hack.🔥"
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
            "☄️Color Trading Mai Maine Number Prediction + Big Small ✅ Hack Banwaye Apke liye ⭐️⭐️ "
            "Yeh Bilkul Apko Free Milegaa , Niche Diye Gaye Button Click Karo And Lattest Hack ko Download Karo 🌟⚡️"
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⭐️SIKKIM VIP HACK⭐️", callback_data="sikkim_hack")],
            [InlineKeyboardButton("⭐️GOA STAR HACK⭐️", callback_data="goa_hack")],
            [InlineKeyboardButton("⭐️DIUWIN GRAND HACK⭐️", callback_data="diuwin_hack")],
            [InlineKeyboardButton("⭐️OKWIN SURE HACK⭐️", callback_data="okwin_hack")]
        ]),
        parse_mode="MarkdownV2"
    )

# Function to handle button interactions
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge button press

    # Video file IDs, audio file links, and captions for each hack
    hack_data = {
        "sikkim_hack": {
            "video": "BAACAgUAAxkBAAIFQ2eAOe5opaSq7JJdWVqrLC-X0LEOAAIsFQACUi-YV2dFPleZscusNgQ",
            "caption": make_bold("Here is your SIKKIM VIP HACK video! 🎮"),
            "audio": "CQACAgUAAxkBAAIKQ2eNY9Se9WaLmzmPVG6vD1JGZi5oAALxFQACS0BoVG84wlgGFCiaNgQ",
            "apk": "BQACAgUAAxkBAAIKOWeNYt3Hh-pc0E3HGcJqid-rt64tAALlFQAC4mFgVExCI76lQP2zNgQ",
            "apk_caption": make_bold("Install this APK to complete the setup for SIKKIM VIP HACK 📱")
        },
        "goa_hack": {
            "video": "BAACAgUAAxkBAAIFQWeAOdn7lqUmBq-ITbqTadYrxY_UAAIqFQACUi-YV0DfcIG18QsTNgQ",
            "caption": make_bold("Here is your GOA STAR HACK video! 🎮"),
            "audio": "CQACAgUAAxkBAAIKQ2eNY9Se9WaLmzmPVG6vD1JGZi5oAALxFQACS0BoVG84wlgGFCiaNgQ",
            "apk": "BQACAgUAAxkBAAIKPmeNYzYxYUVYMEldWvBLQCUoDB0zAALzFQAC4mFgVBTvuQZ4VE2wNgQ",
            "apk_caption": make_bold("Install this APK to complete the setup for GOA STAR HACK 📱")
        },
        "diuwin_hack": {
            "video": "BAACAgUAAxkBAAIFRWeAOf_EbK1vELSPelyURuedS4mpAAIlFQACUi-YV1tU16AUCZT6NgQ",
            "caption": make_bold("Here is your DIUWIN GRAND HACK video!"),
            "audio": "CQACAgUAAxkBAAIKQ2eNY9Se9WaLmzmPVG6vD1JGZi5oAALxFQACS0BoVG84wlgGFCiaNgQ",
            "apk": "BQACAgUAAxkBAAIKPGeNYxcmM3Ip9wRT-PEodkkG3ktoAALsFQAC4mFgVL9Z2GE_pzejNgQ",
            "apk_caption": make_bold("Install this APK to complete the setup for DIUWIN GRAND HACK")
        },
        "okwin_hack": {
            "video": "BAACAgUAAxkBAAIFR2eAOhB1gie6sAYYsQdImO4OD5uvAAInFQACUi-YV6lnP25EkisMNgQ",
            "caption": make_bold("Here is your OKWIN SURE HACK video!"),
            "audio": "CQACAgUAAxkBAAIKQ2eNY9Se9WaLmzmPVG6vD1JGZi5oAALxFQACS0BoVG84wlgGFCiaNgQ",
            "apk": "BQACAgUAAxkBAAIKQGeNY0ozqMEmNwT-01sQbeBeNrrXAAL9FQAC4mFgVEqJt00HNMD6NgQ",
            "apk_caption": make_bold("Install this APK to complete the setup for OKWIN SURE HACK")
        }
    }

    if query.data in hack_data:
        hack = hack_data[query.data]

        # Send the video using file ID
        await query.message.reply_video(
            video=hack["video"],
            caption=hack["caption"],
            parse_mode="MarkdownV2"
        )

        # Send the audio with its caption
        await query.message.reply_audio(
            audio=hack["audio"],
        )

        # Send the APK file link
        await query.message.reply_document(
            document=hack["apk"],
            caption=hack["apk_caption"],
            parse_mode="MarkdownV2"
        )

# Flask endpoints
@app.route('/')
def home():
    return "Bot is running!"

@app.route('/test')
def test():
    return "Test endpoint active!"

# Run Telegram bot
def run_telegram_bot():
    application = ApplicationBuilder().token("7446057407:AAFp5hofMUG_F_Z-VhZjYnzX8MeJ_xvy43M").build()
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
