from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Function to handle the received video
async def handle_video(update, context):
    video_message = update.message.video
    file_id = video_message.file_id
    print(f"File ID: {file_id}")  # You can store it in a database or a file.
    await update.message.reply_text(f"Here is your File ID: {file_id}")

# Initialize the bot
def main():
    application = ApplicationBuilder().token("7446057407:AAFsS-f-_lPLgeXM5H7ox59oCofa8cniTGk").build()

    # Handler for video messages
    application.add_handler(MessageHandler(filters.VIDEO, handle_video))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
