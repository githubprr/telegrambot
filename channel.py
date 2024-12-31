from telethon import TelegramClient, errors

# Replace with your credentials
API_ID = '21544423'
API_HASH = '85c83dc2f00378beb87d782923f520a1'
PHONE_NUMBER = '+917488868338'  # Your personal phone number
CHANNEL_LINK = 'https://t.me/+ceBWQcz7OnU2ZWFl'  # Replace with your channel link
MESSAGE = """
💥 **Get Our LZR Hack App Now!** 💥  
🔥 **Recover Your Money in Minutes!** 🔥  
Don’t let fraud or losses hold you back! 🚀  
**LZR Hack App** is here to help you recover your funds in no time. 🔐  
👉 **Download now and get your money back!** 💸

📌 Join Our Group/Channel for more info: {group_link}
"""

# Initialize Telegram client for your personal account
client = TelegramClient('personal_account', API_ID, API_HASH)

async def send_messages():
    try:
        print("Connecting to Telegram...")
        await client.start(phone=PHONE_NUMBER)
        print("Connected.")

        print("Fetching channel members...")
        members = await client.get_participants(CHANNEL_LINK)

        print(f"Found {len(members)} members. Sending messages...")
        for user in members:
            try:
                if user.is_self or user.bot:
                    continue
                await client.send_message(user.id, MESSAGE)
                print(f"Message sent to {user.id}")
            except errors.FloodWaitError as e:
                print(f"FloodWaitError: Sleeping for {e.seconds} seconds")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f"Failed to send message to {user.id}: {e}")
        
        print("All messages sent.")
    except Exception as e:
        print(f"Error: {e}")

with client:
    client.loop.run_until_complete(send_messages())
