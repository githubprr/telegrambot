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
    escaped_text = re.sub(r"([_*()~`>#+\-=|{}.!])", r"\\\1", text)  # Escape reserved characters
    return f"*{escaped_text}*"

# Function to create hack buttons menu
def get_hack_buttons_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✅SIKKIM VIP HACK✅", callback_data="sikkim_hack")],
        [InlineKeyboardButton("✅GOA STAR HACK✅", callback_data="goa_hack")],
        [InlineKeyboardButton("✅DIUWIN GRAND HACK✅", callback_data="diuwin_hack")],
        [InlineKeyboardButton("✅OKWIN SURE HACK✅", callback_data="okwin_hack")]
    ])

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Welcome message with bold text
    await context.bot.send_message(
        chat_id=chat_id,
        text=make_bold("Welcome to the 🤑 Casino Hack Bot 🎲"),
        parse_mode="MarkdownV2"
    )

    # Send hack buttons menu
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://sstournaments.com/piyush/image2.jpg",
        caption=make_bold(
            "🛍 Apna Choice ke according Color Prediciton Master Hack choose karo.💸 "
            "Tumhare paas mauka hai profit wale VIP Hacks Ko Free Mai Lene Ka."
        ),
        reply_markup=get_hack_buttons_menu(),
        parse_mode="MarkdownV2"
    )

# Function to handle button interactions
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge button press

    # Video, audio, and APK data for each hack
    hack_data = {
        "sikkim_hack": {
            "video": "BAACAgUAAxkBAAIFQ2eAOe5opaSq7JJdWVqrLC-X0LEOAAIsFQACUi-YV2dFPleZscusNgQ",
            "caption": make_bold("Here is your SIKKIM VIP HACK video! 🎮"),
            "audio": "CQACAgUAAxkBAAIFSWeAOiQz7gvpHAWOjqCJM0HobBtqAAKaEgACmJEAAVR7IngSjkXofTYE",
            "audio_caption": make_bold("Listen to activate hack 🌟 Register: http://www.sikkim7.com/#/register?invitationCode=73728400111"),
            "apk": "BQACAgUAAxkBAAIFUWeAOmX_kgABXmwrS5tReBEf1zPKawACohIAApiRAAFUDlhg__DwTCs2BA",
            "apk_caption": make_bold("Install this APK to complete the setup for SIKKIM VIP HACK 📱")
        },
        "goa_hack": {
            "video": "BAACAgUAAxkBAAIFQWeAOdn7lqUmBq-ITbqTadYrxY_UAAIqFQACUi-YV0DfcIG18QsTNgQ",
            "caption": make_bold("Here is your GOA STAR HACK video! 🎮"),
            "audio": "CQACAgUAAxkBAAIFS2eAOjPn0KdFdeEAAWMuUweLDLggNgACmxIAApiRAAFU6SxTFtK5DUk2BA",
            "audio_caption": make_bold("Listen to activate hack 🌟 Register: https://www.bing009.com/#/register?invitationCode=416623809168"),
            "apk": "BQACAgUAAxkBAAIFU2eAOnbRKkBMcXxXwamNLWZ1qrLFAAKjEgACmJEAAVRN0eyjLcLhSDYE",
            "apk_caption": make_bold("Install this APK to complete the setup for GOA STAR HACK 📱")
        },
        "diuwin_hack": {
            "video": "BAACAgUAAxkBAAIFRWeAOf_EbK1vELSPelyURuedS4mpAAIlFQACUi-YV1tU16AUCZT6NgQ",
            "caption": make_bold("Here is your DIUWIN GRAND HACK video!"),
            "audio": "CQACAgUAAxkBAAIFTWeAOkLGn32xjcK6A3BEzCqFs5a3AAKcEgACmJEAAVSC4M7nMebJ0DYE",
            "audio_caption": make_bold("Listen to activate hack. Register: https://diuwinapp.pro/#/register?invitationCode=42677100202"),
            "apk": "BQACAgUAAxkBAAIFVWeAOoTBs2wb6JfzAlwU7UNBWydqAAKkEgACmJEAAVSs9mEiy1S7kTYE",
            "apk_caption": make_bold("Install this APK to complete the setup for DIUWIN GRAND HACK")
        },
        "okwin_hack": {
            "video": "BAACAgUAAxkBAAIFR2eAOhB1gie6sAYYsQdImO4OD5uvAAInFQACUi-YV6lnP25EkisMNgQ",
            "caption": make_bold("Here is your OKWIN SURE HACK video!"),
            "audio": "CQACAgUAAxkBAAIFT2eAOlD14d3qKLvfnxQOi-qtVdTeAAKdEgACmJEAAVTYKP70xt2zojYE",
            "audio_caption": make_bold("Listen to activate hack. Register: https://www.okowin.com/#/register?invitationCode=282452739393"),
            "apk": "BQACAgUAAxkBAAIFV2eAOpPDdEHIne843nNqHhiKf6InAAKlEgACmJEAAVSOa7SdBd1b2TYE",
            "apk_caption": make_bold("Install this APK to complete the setup for OKWIN SURE HACK")
        }
    }

    # Respond based on the hack button clicked
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
            caption=hack["audio_caption"],
            parse_mode="MarkdownV2"
        )

        # Send the APK file link
        await query.message.reply_document(
            document=hack["apk"],
            caption=hack["apk_caption"],
            parse_mode="MarkdownV2"
        )

    # Always resend the bottom menu after any action
    await query.message.reply_text(
        "Choose an option from the menu below:",
        reply_markup=get_hack_buttons_menu(),
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
    BOT_TOKEN = "7446057407:AAFp5hofMUG_F_Z-VhZjYnzX8MeJ_xvy43M"
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.run_polling()

# Run Flask server
def run_flask():
    import os
    port = int(os.environ.get("PORT", 10000))  # Use dynamic port if available
    app.run(host='0.0.0.0', port=port)

# Main entry point
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    run_telegram_bot()
