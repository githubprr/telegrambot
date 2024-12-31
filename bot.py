import os
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Initialize Flask web server
app = Flask(__name__)

# A dictionary to store file IDs for different media types
media_file_ids = {
    "sikkim_hack": {"video": None, "audio": None, "image": None, "apk": None},
    "goa_hack": {"video": None, "audio": None, "image": None, "apk": None},
    "diuwin_hack": {"video": None, "audio": None, "image": None, "apk": None},
    "okwin_hack": {"video": None, "audio": None, "image": None, "apk": None}
}

# Function to handle the start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="Welcome to the 🤑 Casino Hack Bot 🎲")

    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://drive.google.com/uc?id=19p7j4tb9vIz_Ff6vAbcA_cMgnQLasC0O",
        caption="**Yeh mera main channel hai, jaha mein apna kaam dikhata hu. Mere channel ko subscribe kree, aur latest khabre prapt kree.🔥**",
        reply_markup=InlineKeyboardMarkup([ 
            [InlineKeyboardButton("✅SUBSCRIBE✅", url="https://t.me/+5icz2F7eIn0zZDI1")]
        ])
    )

    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://sstournaments.com/piyush/image2.jpg",
        caption="**🛍 Apna Choice ke according Color Prediciton Master Hack choose karo.💸 Tumhare paas mauka hai profit wale VIP Hacks Ko Free Mai Lene Ka.**",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✅SIKKIM VIP HACK✅", callback_data="sikkim_hack")],
            [InlineKeyboardButton("✅GOA STAR HACK✅", callback_data="goa_hack")],
            [InlineKeyboardButton("✅DIUWIN GRAND HACK✅", callback_data="diuwin_hack")],
            [InlineKeyboardButton("✅OKWIN SURE HACK✅", callback_data="okwin_hack")]
        ])
    )

# Function to handle button clicks
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the button click

    media_urls = {
        "sikkim_hack": {
            "video": "https://sstournaments.com/piyush/sikkimhack.mp4",
            "audio": "https://sstournaments.com/piyush/sikkimaudio.mp3",
            "image": "https://sstournaments.com/piyush/sikkimimage.jpg",
            "apk": "https://sstournaments.com/piyush/sikkim1.apk"
        },
        "goa_hack": {
            "video": "https://sstournaments.com/piyush/goahack.mp4",
            "audio": "https://sstournaments.com/piyush/goahack.mp3",
            "image": "https://sstournaments.com/piyush/goaimage.jpg",
            "apk": "https://sstournaments.com/piyush/goagame.apk"
        },
        "diuwin_hack": {
            "video": "https://sstournaments.com/piyush/diuwinhack.mp4",
            "audio": "https://sstournaments.com/piyush/diuwinhack.mp3",
            "image": "https://sstournaments.com/piyush/diuwinimage.jpg",
            "apk": "https://sstournaments.com/piyush/diuwin1.apk"
        },
        "okwin_hack": {
            "video": "https://sstournaments.com/piyush/okwinhack.mp4",
            "audio": "https://sstournaments.com/piyush/okwinhack.mp3",
            "image": "https://sstournaments.com/piyush/okwinimage.jpg",
            "apk": "https://sstournaments.com/piyush/okwin4.apk"
        }
    }

    hack_type = query.data  # e.g., 'sikkim_hack'

    # Iterate over media types (video, audio, image, apk)
    for media_type in ["video", "audio", "image", "apk"]:
        media_url = media_urls[hack_type][media_type]
        file_id_key = media_file_ids[hack_type].get(media_type)

        if file_id_key:
            # Use stored file_id for sending media
            await send_media_by_file_id(query, media_type, file_id_key)
        else:
            # Upload the media for the first time and store the file_id
            media = await upload_and_store_media(context, query.message.chat.id, media_type, media_url, hack_type)
            file_id = media.file_id
            media_file_ids[hack_type][media_type] = file_id
            await send_media_by_file_id(query, media_type, file_id)

# Function to upload media and store file_id
async def upload_and_store_media(context, chat_id, media_type, media_url, hack_type):
    if media_type == "video":
        media = await context.bot.send_video(chat_id=chat_id, video=media_url, caption=f"Here is your {hack_type} video! 🎮")
    elif media_type == "audio":
        media = await context.bot.send_audio(chat_id=chat_id, audio=media_url, caption=f"Here is your {hack_type} audio! 🎧")
    elif media_type == "image":
        media = await context.bot.send_photo(chat_id=chat_id, photo=media_url, caption=f"Here is your {hack_type} image! 🖼")
    elif media_type == "apk":
        media = await context.bot.send_document(chat_id=chat_id, document=media_url, caption=f"Here is your {hack_type} APK! 📱")

    return media

# Function to send media by file_id
async def send_media_by_file_id(query, media_type, file_id):
    if media_type == "video":
        await query.message.reply_video(video=file_id, caption="Here's your requested video!")
    elif media_type == "audio":
        await query.message.reply_audio(audio=file_id, caption="Here's your requested audio!")
    elif media_type == "image":
        await query.message.reply_photo(photo=file_id, caption="Here's your requested image!")
    elif media_type == "apk":
        await query.message.reply_document(document=file_id, caption="Here's your requested APK!")

# Initialize Flask web server
app = Flask(__name__)

# Main entry point to run the bot
if __name__ == '__main__':
    # Set up the Telegram bot
    application = ApplicationBuilder().token('7446057407:AAFsS-f-_lPLgeXM5H7ox59oCofa8cniTGk').build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Run the bot with polling
    application.run_polling()

    # Set up a basic Flask route to bind the service to a port
    @app.route('/')
    def home():
        return "Bot is running..."

    # Run the Flask web server to listen on a specified port (5000 by default)
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
