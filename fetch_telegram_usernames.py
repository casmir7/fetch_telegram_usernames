from telethon import TelegramClient
import logging
import asyncio
import os

# Set up logging for better visibility
logging.basicConfig(level=logging.INFO)

# Load sensitive data from environment variables
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
phone_number = os.getenv('TELEGRAM_PHONE_NUMBER')

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Target group (use the correct group ID or username)
target_group = '-1002473255678'  # Replace with your group ID or username

async def get_usernames_from_history():
    """Fetch and log usernames from the group's chat history."""
    try:
        group = await client.get_entity(target_group)
        messages = await client.get_messages(group, limit=1000)

        for message in messages:
            user = await message.get_sender()
            if user and user.username:
                logging.info('Username: {}'.format(user.username))
            else:
                logging.info('No username found for this message')
    except Exception as e:
        logging.error('An error occurred: {}'.format(e))

async def main():
    """Start the Telegram client and fetch usernames from the group."""
    try:
        await client.start(phone_number)
        logging.info("Client started. Fetching chat history...")
        await get_usernames_from_history()
    finally:
        await client.disconnect()
        logging.info("Client disconnected.")

if __name__ == "__main__":  # <-- Fixed typo here
    asyncio.run(main())
