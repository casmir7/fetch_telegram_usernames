# Fetch Telegram Usernames from Group Chat

This Python script uses the [Telethon](https://github.com/LonamiWebs/Telethon) library to connect to a Telegram group and extract usernames from the latest 1000 messages.

---

## 📦 Features

- Connects securely to Telegram via the Telethon API
- Fetches up to 1000 recent messages from a specific group
- Logs usernames of message senders
- Handles cases where usernames are not available
- Designed with async for performance
- Credentials are hidden using environment variables

---

## 🧰 Requirements

- Python 3.7+
- Install dependencies using pip:

```bash
pip install telethon
