import asyncio
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Function to send scheduled messages
async def send_message_at_specific_time(context: ContextTypes.DEFAULT_TYPE, chat_id, message_type, content, caption, buttons):
    now = datetime.now()
    scheduled_time = datetime.strptime(content["datetime"], "%Y-%m-%d %H:%M")

    # Calculate delay
    delay = (scheduled_time - now).total_seconds()

    if delay > 0:  # Wait if the scheduled time is in the future
        print(f"Waiting {delay} seconds until {content['datetime']} to send message.")
        await asyncio.sleep(delay)

    # Send the message
    if message_type == "photo":
        with open(content["path"], "rb") as file:
            await context.bot.send_photo(
                chat_id=chat_id,
                photo=file,
                caption=caption,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
    elif message_type == "video":
        with open(content["path"], "rb") as file:
            await context.bot.send_video(
                chat_id=chat_id,
                video=file,
                caption=caption,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
    print(f"Message sent at {datetime.now()} for scheduled time {content['datetime']}.")

# Function to handle the start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Instant message with buttons
    await context.bot.send_message(chat_id=chat_id, text="Welcome to the 🤑 Casino Hack Bot 🎲")

    # First instant photo message before the buttons
    await context.bot.send_photo(
        chat_id=chat_id,
        photo=open(r"c:\Users\Piyus\Documents\photo_2024-08-24_01-01-19.jpg", "rb"),
        caption="**Yeh mera main channel hai, jaha mein apna kaam dikhata hu. Mere channel ko subscribe kree, aur latest khabre prapt kree.🔥**",
        reply_markup=InlineKeyboardMarkup([ 
            [InlineKeyboardButton("✅SUBSCRIBE✅", url="https://t.me/+5icz2F7eIn0zZDI1")],
            [InlineKeyboardButton("✅SUBSCRIBE✅", url="https://t.me/+5icz2F7eIn0zZDI1")]
        ])
    )

    # Instant photo message with interactive buttons (This is the only instance of photo sending now)
    await context.bot.send_photo(
        chat_id=chat_id,
        photo=open(r"C:\Users\Piyus\Downloads\hackimage.jpg", "rb"),
        caption="**🛍 Apna Choice ke according Color Prediciton Master Hack choose karo.💸 Tumhare paas mauka hai profit wale VIP Hacks Ko Free Mai Lene Ka.**",
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
            video=open(r"C:\Users\Piyus\Downloads\sikkimgamevideo.mp4", "rb"),
            caption="Here is your SIKKIM VIP HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Download HACK", url="https://drive.google.com/file/d/1yHAF-20Yc8HktwHbwUwuWUSJbNp-KKMa/view?usp=drive_link")],
                [InlineKeyboardButton("🆘HELP🆘", url="https://t.me/Vishuskills")],
            ])
        )

        # Send an audio file after the video
        await query.message.reply_audio(
            audio=open(r"C:\Users\Piyus\Downloads\sikkimaudio.mp3", "rb"),
            caption="IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟Hack Register Link ✨ http://www.sikkim7.com/#/register?invitationCode=73728400111"
        )

    elif query.data == "goa_hack":
        # Send video first
        await query.message.reply_video(
            video=open(r"C:\Users\Piyus\Downloads\sikkimgamevideo.mp4", "rb"),
            caption="Here is your GOA STAR HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Download HACK", url="https://drive.google.com/file/d/1hfS4PQAhxB-bR7F6cQ6zpM1Mtywb-mWI/view?usp=drive_link")],
                [InlineKeyboardButton("🆘HELP🆘", url="https://t.me/Vishuskills")],
            ])
        )

        # Send an audio file after the video
        await query.message.reply_audio(
            audio=open(r"C:\Users\Piyus\Downloads\sikkimaudio.mp3", "rb"),
            caption="IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟Hack Register Link ✨ http://www.sikkim7.com/#/register?invitationCode=73728400111"
        )

    elif query.data == "diuwin_hack":
        # Send video first
        await query.message.reply_video(
            video=open(r"C:\Users\Piyus\Downloads\sikkimgamevideo.mp4", "rb"),
            caption="Here is your DIUWIN GRAND HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Download HACK", url="https://drive.google.com/file/d/1txLIhYbw0C2wD52Ccyg7w0ztZ_xasWdB/view?usp=drive_link")],
                [InlineKeyboardButton("🆘HELP🆘", url="https://t.me/Vishuskills")],
            ])
        )

        # Send an audio file after the video
        await query.message.reply_audio(
            audio=open(r"C:\Users\Piyus\Downloads\sikkimaudio.mp3", "rb"),
            caption="IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟Hack Register Link ✨ http://www.sikkim7.com/#/register?invitationCode=73728400111"
        )

    elif query.data == "okwin_hack":
        # Send video first
        await query.message.reply_video(
            video=open(r"C:\Users\Piyus\Downloads\sikkimgamevideo.mp4", "rb"),
            caption="Here is your OKWIN SURE HACK video! 🎮",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Download HACK", url="https://drive.google.com/file/d/1mtrUToC-w4IytEswyEVh_PmFpe13qOp0/view?usp=drive_link")],
                [InlineKeyboardButton("🆘HELP🆘", url="https://t.me/Vishuskills")],
            ])
        )

        # Send an audio file after the video
        await query.message.reply_audio(
            audio=open(r"C:\Users\Piyus\Downloads\sikkimaudio.mp3", "rb"),
            caption="IMPORTANT AUDIO ⭐️⭐️Listen Full For Activate Hack 🌟Hack Register Link ✨ http://www.sikkim7.com/#/register?invitationCode=73728400111"
        )

    # Schedule messages with their respective buttons (not needed for button handler, kept for your reference)
    schedule = [
        {
            "datetime": "2024-12-31 18:24",
            "type": "photo",
            "path": r"C:\Users\Piyus\Documents\photo_2024-08-24_01-01-19.jpg",
            "caption": "Scheduled Photo 1",
            "buttons": [
                [InlineKeyboardButton("✅SUBSCRIBE✅", url="https://example.com/1")],
                [InlineKeyboardButton("✅SUBSCRIBE✅", url="https://example.com/share1")],
                [InlineKeyboardButton("✅SUBSCRIBE✅", url="https://example.com/download1")]
            ]
        },
        {
            "datetime": "2024-12-31 18:25",
            "type": "video",
            "path": r"C:\Users\Piyus\Documents\videoplayback.mp4",
            "caption": "Scheduled Video 1",
            "buttons": [
                [InlineKeyboardButton("✅SUBSCRIBE✅", url="https://example.com/2")],
                [InlineKeyboardButton("✅SUBSCRIBE✅", url="https://example.com/share2")],
                [InlineKeyboardButton("✅SUBSCRIBE✅", url="https://example.com/download2")]
            ]
        }
    ]

    # Send the scheduled messages
    for content in schedule:
        await send_message_at_specific_time(context, chat_id, content["type"], content, content["caption"], content["buttons"])

# Main entry point to run the bot
if __name__ == '__main__':
    application = ApplicationBuilder().token('7446057407:AAFsS-f-_lPLgeXM5H7ox59oCofa8cniTGk').build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Run the bot
    application.run_polling()
