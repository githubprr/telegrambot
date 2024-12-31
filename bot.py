import os
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
    await context.bot.send_message(chat_id=chat_id, text="Welcome to the 🤑 Casino Hack Bot 🎲")

    # First instant photo message before the buttons
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://drive.google.com/uc?id=19p7j4tb9vIz_Ff6vAbcA_cMgnQLasC0O",
        caption="Yeh mera main channel hai, jaha mein apna kaam dikhata hu. Mere channel ko subscribe kree, aur latest khabre prapt kree.🔥",
        reply_markup=InlineKeyboardMarkup([ 
            [InlineKeyboardButton("✅SUBSCRIBE✅", url="https://t.me/+5icz2F7eIn0zZDI1")]
        ])
    )

    # Instant photo message with interactive buttons
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://sstournaments.com/piyush/image2.jpg",
        caption="🛍 **Apna** Choice ke according Color Prediciton Master Hack choose karo.💸 Tumhare paas mauka hai profit wale VIP Hacks Ko Free Mai Lene Ka.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✅SIKKIM VIP HACK✅", callback_data="sikkim_hack")],
            [InlineKeyboardButton("✅GOA STAR HACK✅", callback_data="goa_hack")],
            [InlineKeyboardButton("✅DIUWIN GRAND HACK✅", callback_data="diuwin_hack")],
            [InlineKeyboardButton("✅OKWIN SURE HACK✅", callback_data="okwin_hack")]  # Added OKWIN button
        ])
    )

# Function to handle button clicks
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the button click

    # Checking the callback data and sending video + audio
    if query.data == "sikkim_hack":
        # Send video first
        await query.message.reply_video(
            video="https://sstournaments.com/piyush/sikkimhack.mp4",
            caption="Here is your SIKKIM VIP HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Download HACK", url="https://drive.google.com/file/d/1_yyTL1jguLINDKf4WqokSIV1RBsQxtVV/view?usp=sharing")],
                [InlineKeyboardButton("🆘HELP🆘", url="https://t.me/Vishuskills")],
            ])
        )

        # Send an audio file after the video
        await query.message.reply_audio(
            audio="https://sstournaments.com/piyush/sikkimaudio.mp3",
            caption="IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟Hack \n Register Link ✨ http://www.sikkim7.com/#/register?invitationCode=73728400111"
        )

    elif query.data == "goa_hack":
        # Send video first
        await query.message.reply_video(
            video="https://sstournaments.com/piyush/goahack.mp4",
            caption="Here is your GOA STAR HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Download HACK", url="https://drive.google.com/file/d/1rFi61Rn3Hkd_Z20Tcwo9cwWhufdeEmVk/view?usp=sharing")],
                [InlineKeyboardButton("🆘HELP🆘", url="https://t.me/Vishuskills")],
            ])
        )

        # Send an audio file after the video
        await query.message.reply_audio(
            audio="https://sstournaments.com/piyush/goahack.mp3",
            caption="IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟Hack \n Register Link ✨ http://www.sikkim7.com/#/register?invitationCode=73728400111"
        )

    elif query.data == "diuwin_hack":
        # Send video first
        await query.message.reply_video(
            video="https://sstournaments.com/piyush/diuwinhack.mp4",
            caption="Here is your DIUWIN GRAND HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Download HACK", url="https://drive.google.com/file/d/1lCW4quCtpVYE25xp6pO-kUGUJhriaJ5Z/view?usp=sharing")],
                [InlineKeyboardButton("🆘HELP🆘", url="https://t.me/Vishuskills")],
            ])
        )

        # Send an audio file after the video
        await query.message.reply_audio(
            audio="https://sstournaments.com/piyush/diuwinhack.mp3",
            caption="IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟Hack \n Register Link ✨ http://www.sikkim7.com/#/register?invitationCode=73728400111"
        )

    elif query.data == "okwin_hack":
        # Send video first
        await query.message.reply_video(
            video="https://sstournaments.com/piyush/okwinhack.mp4",
            caption="Here is your OKWIN SURE HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Download HACK", url="https://drive.google.com/file/d/1C1mimf21Eecb_2pTgaTehTqDssOaAKa_/view?usp=sharing")],
                [InlineKeyboardButton("🆘HELP🆘", url="https://t.me/Vishuskills")],
            ])
        )

        # Send an audio file after the video
        await query.message.reply_audio(
            audio="https://sstournaments.com/piyush/okwinhack.mp3",
            caption="IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟Hack \n Register Link ✨ http://www.sikkim7.com/#/register?invitationCode=73728400111"
        )


# Function to run the bot in a separate thread
def run_bot():
    application = ApplicationBuilder().token('7446057407:AAFsS-f-_lPLgeXM5H7ox59oCofa8cniTGk').build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Run the bot with polling
    application.run_polling()

# Main entry point to run the Flask web server and the bot
if __name__ == '__main__':
    # Start the bot in a separate thread
    threading.Thread(target=run_bot).start()

    # Set up a basic Flask route to bind the service to a port
    @app.route('/')
    def home():
        return "Bot is running..."

    # Run the Flask web server to listen on a specified port (5000 by default)
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
