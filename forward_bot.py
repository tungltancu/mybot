import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

# Load biến môi trường từ file .env
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL")

# Khởi tạo bot client
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Lắng nghe tin nhắn mới từ channel nguồn
@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    try:
        await client.send_message(TARGET_CHANNEL, event.message)
        print("✔ Tin nhắn đã được chuyển tiếp.")
    except Exception as e:
        print("❌ Lỗi:", e)

print("🤖 Bot đang chạy...")
client.run_until_disconnected()
