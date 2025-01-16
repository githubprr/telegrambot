import os
import re
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

# Flask app
app = Flask(__name__)

# Helper function to make text bold
def make_bold(text):
    escaped_text = re.sub(r"([_*()~`>#+\-=|{}.!])", r"\\\1", text)  # Escape reserved characters
    return f"*{escaped_text}*"

# Start command handler
async def start(update: Update, context):
    chat_id = update.effective_chat.id

    # Welcome message
    await context.bot.send_message(
        chat_id=chat_id,
        text=make_bold("🎉 Welcome to the 🤑 Casino Hack Bot 🎲"),
        parse_mode="MarkdownV2"
    )

    # Send an image with subscription button
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

# Callback query handler
async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()  # Acknowledge the button press

    # Respond with a simple message
    await query.edit_message_text(
        text=make_bold("You clicked a button! 🎉"),
        parse_mode="MarkdownV2"
    )

# Flask webhook endpoint
@app.route(f"/webhook/{os.getenv('BOT_TOKEN')}", methods=["POST"])
def telegram_webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        bot.application.process_update(update)
    return "ok", 200

# Main function to set up the bot
async def main():
    # Create the application
    application = Application.builder().token(os.getenv("BOT_TOKEN")).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Start the webhook
    await application.start()
    await application.updater.start_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        webhook_url=f"{os.getenv('WEBHOOK_URL')}/webhook/{os.getenv('BOT_TOKEN')}"
    )

    # Run the application
    await application.updater.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
