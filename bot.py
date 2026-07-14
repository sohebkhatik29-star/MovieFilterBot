import asyncio
import os
import sys

# 1. Event Loop Setup (Python 3.14 Fix)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# 2. Imports
from flask import Flask
from threading import Thread
from pyrogram import Client, filters

# 3. Configs
API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
MASTER_TOKEN = os.environ.get("MASTER_TOKEN", "")
PORT = int(os.environ.get("PORT", 8080))

# 4. Web Server
app = Flask(__name__)
@app.route('/')
def home(): return "Bot is Running!"
def run_web(): app.run(host='0.0.0.0', port=PORT)

# 5. Bot Client
# API_ID ko yahan convert kar rahe hain taaki error na aaye
bot = Client("master_bot", api_id=int(API_ID) if API_ID else 0, api_hash=API_HASH, bot_token=MASTER_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Bot Live Hai!")

if __name__ == "__main__":
    if not API_ID or not API_HASH or not MASTER_TOKEN:
        print("ERROR: Environment Variables Missing!")
        sys.exit(1)
    
    Thread(target=run_web, daemon=True).start()
    bot.run()

