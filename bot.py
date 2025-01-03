# import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Initialize Flask web server
app = Flask(__name__)


# Function to handle the start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Instant message with buttons
    await context.bot.send_message(chat_id=chat_id,
                                   text="Welcome to the 🤑 Casino Hack Bot 🎲")

    # First instant photo message before the buttons
    await context.bot.send_photo(
        chat_id=chat_id,
        photo=
        "https://drive.google.com/uc?id=19p7j4tb9vIz_Ff6vAbcA_cMgnQLasC0O",
        caption=
        "<b>Yeh mera main channel hai, jaha mein apna kaam dikhata hu. Mere channel ko subscribe kree, aur latest khabre prapt kree.🔥</b>",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("✅SUBSCRIBE✅",
                                 url="https://t.me/+5icz2F7eIn0zZDI1")
        ]]))

    # Instant photo message with interactive buttons
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://sstournaments.com/piyush/image2.jpg",
        caption=
        "🛍 **Apna** Choice ke according Color Prediciton Master Hack choose karo.💸 Tumhare paas mauka hai profit wale VIP Hacks Ko Free Mai Lene Ka.",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("✅SIKKIM VIP HACK✅",
                                     callback_data="sikkim_hack")
            ],
            [
                InlineKeyboardButton("✅GOA STAR HACK✅",
                                     callback_data="goa_hack")
            ],
            [
                InlineKeyboardButton("✅DIUWIN GRAND HACK✅",
                                     callback_data="diuwin_hack")
            ],
            [
                InlineKeyboardButton("✅OKWIN SURE HACK✅",
                                     callback_data="okwin_hack")
            ]  # Added OKWIN button
        ]))


# Function to handle button clicks
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the button click

    # Checking the callback data and sending video + audio
    if query.data == "sikkim_hack":
        # Send video first
        await query.message.reply_video(
            video="https://sstournaments.com/piyush/okwinhack.mp4",
            caption="Here is your SIKKIM VIP HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "Download HACK",
                        url=
                        "https://drive.google.com/file/d/1_yyTL1jguLINDKf4WqokSIV1RBsQxtVV/view?usp=sharing"
                    )
                ],
                [
                    InlineKeyboardButton("🆘HELP🆘",
                                         url="https://t.me/Vishuskills")
                ],
            ]))

        # Send an audio file after the video
        await query.message.reply_audio(
            audio="https://sstournaments.com/piyush/sikkimaudio.mp3",
            caption=
            "<b>IMPORTANT AUDIO ⭐️⭐️ Listen Full For Activate Hack 🌟 /n Hack Register Link ✨✨ http://www.sikkim7.com/#/register?invitationCode=73728400111</b>"
        )

    elif query.data == "goa_hack":
        # Send video first
        await query.message.reply_video(
            video="https://sstournaments.com/piyush/okwinhack.mp4",
            caption="Here is your GOA STAR HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "Download HACK",
                        url=
                        "https://drive.google.com/file/d/1rFi61Rn3Hkd_Z20Tcwo9cwWhufdeEmVk/view?usp=sharing"
                    )
                ],
                [
                    InlineKeyboardButton("🆘HELP🆘",
                                         url="https://t.me/Vishuskills")
                ],
            ]))

        # Send an audio file after the video
        await query.message.reply_audio(
            audio="https://sstournaments.com/piyush/goahack.mp3",
            caption=
            "IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟Hack Register Link ✨✨https://www.bing009.com/#/register?invitationCode=416623809168"
        )

    elif query.data == "diuwin_hack":
        # Send video first
        await query.message.reply_video(
            video="https://sstournaments.com/piyush/okwinhack.mp4",
            caption="Here is your DIUWIN GRAND HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "Download HACK",
                        url=
                        "https://drive.google.com/file/d/1lCW4quCtpVYE25xp6pO-kUGUJhriaJ5Z/view?usp=sharing"
                    )
                ],
                [
                    InlineKeyboardButton("🆘HELP🆘",
                                         url="https://t.me/Vishuskills")
                ],
            ]))

        # Send an audio file after the video
        await query.message.reply_audio(
            audio="https://sstournaments.com/piyush/diuwinhack.mp3",
            caption=
            "IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟 Hack Register Link ✨✨ https://diuwinapp.pro/#/register?invitationCode=42677100202 /n 24x7 Support ~ @Vishuskills"
        )

    elif query.data == "okwin_hack":
        # Send video first
        await query.message.reply_video(
            video="https://sstournaments.com/piyush/okwinhack.mp4",
            caption="Here is your OKWIN SURE HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
# Function to handle button clicks
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the button click

    # Checking the callback data and sending video + audio
    if query.data == "sikkim_hack":
        # Send updated video for Sikkim
        await query.message.reply_video(
            video="https://file-to-link-nx-ccf8d5eda5c0.herokuapp.com/dl/6777ceb13aaf8bb8c01b0f8b",
            caption="Here is your SIKKIM VIP HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "Download HACK",
                        url="https://drive.google.com/file/d/1_yyTL1jguLINDKf4WqokSIV1RBsQxtVV/view?usp=sharing"
                    )
                ],
                [
                    InlineKeyboardButton("🆘HELP🆘",
                                         url="https://t.me/Vishuskills")
                ],
            ]))

        # Send an audio file after the video
        await query.message.reply_audio(
            audio="https://sstournaments.com/piyush/sikkimaudio.mp3",
            caption="<b>IMPORTANT AUDIO ⭐️⭐️ Listen Full For Activate Hack 🌟 /n Hack Register Link ✨✨ http://www.sikkim7.com/#/register?invitationCode=73728400111</b>"
        )

    elif query.data == "goa_hack":
        # Send updated video for Goa
        await query.message.reply_video(
            video="https://file-to-link-nx-ccf8d5eda5c0.herokuapp.com/dl/6777cede3aaf8bb8c01b0f91",
            caption="Here is your GOA STAR HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "Download HACK",
                        url="https://drive.google.com/file/d/1rFi61Rn3Hkd_Z20Tcwo9cwWhufdeEmVk/view?usp=sharing"
                    )
                ],
                [
                    InlineKeyboardButton("🆘HELP🆘",
                                         url="https://t.me/Vishuskills")
                ],
            ]))

        # Send an audio file after the video
        await query.message.reply_audio(
            audio="https://sstournaments.com/piyush/goahack.mp3",
            caption="IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟Hack Register Link ✨✨https://www.bing009.com/#/register?invitationCode=416623809168"
        )

    elif query.data == "diuwin_hack":
        # Send updated video for DiuWin
        await query.message.reply_video(
            video="https://file-to-link-nx-ccf8d5eda5c0.herokuapp.com/dl/6777ce263aaf8bb8c01b0f86",
            caption="Here is your DIUWIN GRAND HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "Download HACK",
                        url="https://drive.google.com/file/d/1lCW4quCtpVYE25xp6pO-kUGUJhriaJ5Z/view?usp=sharing"
                    )
                ],
                [
                    InlineKeyboardButton("🆘HELP🆘",
                                         url="https://t.me/Vishuskills")
                ],
            ]))

        # Send an audio file after the video
        await query.message.reply_audio(
            audio="https://sstournaments.com/piyush/diuwinhack.mp3",
            caption="IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟 Hack Register Link ✨✨ https://diuwinapp.pro/#/register?invitationCode=42677100202 /n 24x7 Support ~ @Vishuskills"
        )

    elif query.data == "okwin_hack":
        # Send video for OKWIN (unchanged)
        await query.message.reply_video(
            video="https://sstournaments.com/piyush/okwinhack.mp4",
            caption="Here is your OKWIN SURE HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "Download HACK",
                        url="https://drive.google.com/file/d/1C1mimf21Eecb_2pTgaTehTqDssOaAKa_/view?usp=sharing"
                    )
                ],
                [
                    InlineKeyboardButton("🆘HELP🆘",
                                         url="https://t.me/Vishuskills")
                ],
            ]))

        # Send an audio file after the video
        await query.message.reply_audio(
            audio="https://sstournaments.com/piyush/okwinhack.mp3",
            caption="IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟Hack Register Link ✨✨https://www.okowin.com/#/register?invitationCode=282452739393 /n 24x7 Support ~ @Vishuskills"
        )

# Initialize Flask web server
app = Flask(__name__)


@app.route('/')
def home():
    return "Bot is running..."


@app.route('/test')
def test():
    return "Test Bot is running..."


# Main entry point to run the bot


# Function to run the Telegram bot
def run_telegram_bot():
    application = ApplicationBuilder().token(
        '7446057407:AAFsS-f-_lPLgeXM5H7ox59oCofa8cniTGk').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.run_polling()


# Function to run the Flask server
def run_flask():
    # public_url = ngrok.connect(10000)  # Expose Flask app
    # print(f"Flask app is running at {public_url}")
    app.run(host='0.0.0.0', port=10000)


# Main entry point
if __name__ == '__main__':
    # Start Flask and Telegram bot in parallel threads
    threading.Thread(target=run_flask).start()
    run_telegram_bot()
