import re
import random
import asyncio
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# Initialize Flask web server
app = Flask(__name__)

# Bot token and webhook URL
BOT_TOKEN = "7446057407:AAFp5hofMUG_F_Z-VhZjYnzX8MeJ_xvy43M"  # Replace with your bot's token
WEBHOOK_URL = "https://telegrambot-v26n.onrender.com/webhook"  # Replace with your actual domain

# Helper function to make text bold
def make_bold(text):
    escaped_text = re.sub(r"([_*()~`>#+\-=|{}.!])", r"\\\1", text)  # Escape reserved characters
    return f"*{escaped_text}*"

# Function to handle the /start command
async def start(update: Update, context):
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

# Function to handle button interactions and send relevant content (video, audio, apk)
async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()  # Acknowledge button press

    # Data for each hack (video, audio, APK, etc.)
    hack_data = {
        "sikkim_hack": {
            "video": "BAACAgUAAxkBAAIFQ2eAOe5opaSq7JJdWVqrLC-X0LEOAAIsFQACUi-YV2dFPleZscusNgQ",
            "caption": make_bold("🚀 Here is your SIKKIM VIP HACK video! 🎮"),
            "audio": "CQACAgUAAxkBAAIFSWeAOiQz7gvpHAWOjqCJM0HobBtqAAKaEgACmJEAAVR7IngSjkXofTYE",
            "audio_caption": make_bold("🎧 Listen to activate hack 🌟\nRegister: http://www.sikkim7.com/#/register?invitationCode=73728400111"),
            "apk": "BQACAgUAAxkBAAIFUWeAOmX_kgABXmwrS5tReBEf1zPKawACohIAApiRAAFUDlhg__DwTCs2BA",
            "apk_caption": make_bold("📱 Install this APK to complete the setup for *SIKKIM VIP HACK* 🛠️")
        },
        "goa_hack": {
            "video": "BAACAgUAAxkBAAIFQWeAOdn7lqUmBq-ITbqTadYrxY_UAAIqFQACUi-YV0DfcIG18QsTNgQ",
            "caption": make_bold("🚀 Here is your GOA STAR HACK video! 🎮"),
            "audio": "CQACAgUAAxkBAAIFS2eAOjPn0KdFdeEAAWMuUweLDLggNgACmxIAApiRAAFU6SxTFtK5DUk2BA",
            "audio_caption": make_bold("🎧 Listen to activate hack 🌟\nRegister: https://www.bing009.com/#/register?invitationCode=416623809168"),
            "apk": "BQACAgUAAxkBAAIFU2eAOnbRKkBMcXxXwamNLWZ1qrLFAAKjEgACmJEAAVRN0eyjLcLhSDYE",
            "apk_caption": make_bold("📱 Install this APK to complete the setup for *GOA STAR HACK* 🛠️")
        },
        "diuwin_hack": {
            "video": "BAACAgUAAxkBAAIFRWeAOf_EbK1vELSPelyURuedS4mpAAIlFQACUi-YV1tU16AUCZT6NgQ",
            "caption": make_bold("🚀 Here is your DIUWIN GRAND HACK video! 🎮"),
            "audio": "CQACAgUAAxkBAAIFTWeAOkLGn32xjcK6A3BEzCqFs5a3AAKcEgACmJEAAVSC4M7nMebJ0DYE",
            "audio_caption": make_bold("🎧 Listen to activate hack 🌟\nRegister: https://diuwinapp.pro/#/register?invitationCode=42677100202"),
            "apk": "BQACAgUAAxkBAAIFVWeAOoTBs2wb6JfzAlwU7UNBWydqAAKkEgACmJEAAVSs9mEiy1S7kTYE",
            "apk_caption": make_bold("📱 Install this APK to complete the setup for *DIUWIN GRAND HACK* 🛠️")
        },
        "okwin_hack": {
            "video": "BAACAgUAAxkBAAIFR2eAOhB1gie6sAYYsQdImO4OD5uvAAInFQACUi-YV6lnP25EkisMNgQ",
            "caption": make_bold("🚀 Here is your OKWIN SURE HACK video! 🎮"),
            "audio": "CQACAgUAAxkBAAIFT2eAOlD14d3qKLvfnxQOi-qtVdTeAAKdEgACmJEAAVTYKP70xt2zojYE",
            "audio_caption": make_bold("🎧 Listen to activate hack 🌟\nRegister: https://www.okowin.com/#/register?invitationCode=282452739393"),
            "apk": "BQACAgUAAxkBAAIFV2eAOpPDdEHIne843nNqHhiKf6InAAKlEgACmJEAAVSOa7SdBd1b2TYE",
            "apk_caption": make_bold("📱 Install this APK to complete the setup for *OKWIN SURE HACK* 🛠️")
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
            caption=hack["audio_caption"],
            parse_mode="MarkdownV2"
        )

        # Send the APK file link
        await query.message.reply_document(
            document=hack["apk"],
            caption=hack["apk_caption"],
            parse_mode="MarkdownV2"
        )

        # Add a small gamification feature
        game_outcome = random.choice(["win", "lose"])

        if game_outcome == "win":
            await query.message.reply_text(
                text=make_bold("🎉 Congratulations! You've won a bonus! 🎁"),
                parse_mode="MarkdownV2"
            )
            await query.message.reply_text(
                text=make_bold("🚀 Try your luck again and use another hack to get more bonuses! 👇"),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("✅SIKKIM VIP HACK✅", callback_data="sikkim_hack")],
                    [InlineKeyboardButton("✅GOA STAR HACK✅", callback_data="goa_hack")],
                    [InlineKeyboardButton("✅DIUWIN GRAND HACK✅", callback_data="diuwin_hack")],
                    [InlineKeyboardButton("✅OKWIN SURE HACK✅", callback_data="okwin_hack")]
                ]),
                parse_mode="MarkdownV2"
            )
        else:
            await query.message.reply_text(
                text=make_bold("😞 Sorry! You lost this time. Better luck next time! 🍀"),
                parse_mode="MarkdownV2"
            )
            await query.message.reply_text(
                text=make_bold("🚀 Try your luck again and use another hack to get more bonuses! 👇"),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("✅SIKKIM VIP HACK✅", callback_data="sikkim_hack")],
                    [InlineKeyboardButton("✅GOA STAR HACK✅", callback_data="goa_hack")],
                    [InlineKeyboardButton("✅DIUWIN GRAND HACK✅", callback_data="diuwin_hack")],
                    [InlineKeyboardButton("✅OKWIN SURE HACK✅", callback_data="okwin_hack")]
                ]),
                parse_mode="MarkdownV2"
            )

# Setup Flask endpoint to handle webhook
@app.route('/webhook', methods=['POST'])
async def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = Update.de_json(json_str, context.bot)
    await button_handler(update, context)
    return 'OK'

# Set webhook
async def set_webhook():
    await application.bot.set_webhook(WEBHOOK_URL)

# Run the bot
if __name__ == '__main__':
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    asyncio.run(set_webhook())
    app.run(port=8443)
