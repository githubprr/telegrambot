import time
import sys
from telethon import TelegramClient
from telethon.errors import PeerFloodError, MessageTooLongError

# Replace these with your actual API details
api_id = 123456  # Your actual API ID (as an integer)
api_hash = 'your_api_hash'  # Your actual API hash (as a string)
phone_number = '+1234567890'  # Your phone number if needed (for user authentication)
bot_token = 'your_bot_token'  # If you're using a bot, otherwise leave it as an empty string

client = TelegramClient('session_name', api_id, api_hash)

async def send_stylish_message(user_id, group_link):
    """
    Sends a stylish message to a user with the given group/channel link.
    This will simulate a long delay (over 10 minutes) to show the sending status.
    """
    try:
        # Simulate sending with a 10+ minute delay
        print("Sending message... Please wait.")
        time.sleep(600)  # Simulate delay (600 seconds = 10 minutes)

        # Create the stylish message
        message = f"""
        💥 **Get Our LZR Hack App Now!** 💥  
        🔥 **Recover Your Money in Minutes!** 🔥  
        Don’t let fraud or losses hold you back! 🚀  
        **LZR Hack App** is here to help you recover your funds in no time. 🔐  
        👉 **Download now and get your money back!** 💸

        📌 Join Our Group/Channel for more info: {group_link}  
        """

        # Send the message to the user
        await client.send_message(user_id, message)
        print(f"\nMessage sent successfully to {user_id} 🎉")

    except PeerFloodError:
        print(f"Error: You are being rate-limited. Try again later.")
        sys.exit()
    except MessageTooLongError:
        print(f"Error: The message is too long.")
        sys.exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit()

async def handle_user_interaction():
    """
    Handles the user interaction for sending messages.
    """
    try:
        # Ask for user ID and channel/group link to send the message
        print("Welcome to the LZR Hack App Messaging System! 🚀")
        print("===============================================")
        
        user_id = input("Enter the user ID to send message to: ")
        
        if not user_id.isdigit():
            print("Invalid user ID. Please enter a numeric value.")
            return
        
        group_link = input("Enter the channel or group link to include in the message: ")
        
        if not group_link.startswith("https://t.me/"):
            print("Invalid link format. Ensure the link starts with https://t.me/")
            return

        # Confirm and send the message
        print(f"\nPreparing to send message to {user_id}...")
        time.sleep(1)  # Simulating delay for a better user experience
        await send_stylish_message(user_id, group_link)

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
        sys.exit()

async def main():
    """
    Main function to initiate the Telegram client and start the process.
    """
    try:
        await client.start()
        print("\nTelegram Client started successfully!")
        print("==========================================")
        
        # Allow the user to send multiple messages
        while True:
            await handle_user_interaction()
            continue_option = input("\nWould you like to send another message? (y/n): ").lower()
            if continue_option != 'y':
                print("Exiting the system. Goodbye! 👋")
                break
        
    except Exception as e:
        print(f"An error occurred while starting the client: {e}")
        sys.exit()

# Run the Telegram client
with client:
    client.loop.run_until_complete(main())
