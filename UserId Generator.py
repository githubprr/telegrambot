from telethon import TelegramClient
import asyncio

# Replace with your own values
api_id = '21544423'  # Your API ID
api_hash = '85c83dc2f00378beb87d782923f520a1'  # Your API Hash
group_username = 'RadheRahde'  # Group username (without @)

# Define the async function to fetch group members
async def fetch_group_members():
    async with TelegramClient('radhe_session', api_id, api_hash) as client:
        # Attempt to fetch participants in the group
        try:
            async for member in client.iter_participants(group_username):
                print(f"User ID: {member.id}, Username: @{member.username}, Name: {member.first_name}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    asyncio.run(fetch_group_members())
