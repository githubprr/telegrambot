import nest_asyncio
import logging
from telegram.ext import Application, MessageHandler, filters

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a function that will handle messages
async def respond(update, context):
    user_message = update.message.text
    response = f"Received your message: {user_message}"
    await update.message.reply_text(response)

# Main function to start the bot
async def run_bot():
    # Create the application using your bot token
    application = Application.builder().token("8049440485:AAGJCQjwxxRjyD96URN5kqm024Obul8Ex8U").build()  # Replace with your actual bot token

    # Set up the message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

    # Start polling (the bot will wait for incoming messages)
    await application.run_polling()

# Run the bot
if __name__ == "__main__":
    import asyncio
    asyncio.run(run_bot())  # This will properly run the event loop
