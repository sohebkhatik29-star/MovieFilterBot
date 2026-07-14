import asyncio
import os
from flask import Flask
from threading import Thread

# 1. Imports ko yahan se shuru karo
from pyrogram import Client, filters

# --- CONFIGS ---
# Yahan 'int()' hata diya hai, ab ye simple string ban gaya hai
API_ID = os.environ.get("API_ID", "") 
API_HASH = os.environ.get("API_HASH", "")
MASTER_TOKEN = os.environ.get("MASTER_TOKEN", "")
PORT = int(os.environ.get("PORT", 8080))

# --- WEB SERVER ---
app = Flask(__name__)
@app.route('/')
def home(): return "SaaS Bot Live"
def run_web(): app.run(host='0.0.0.0', port=PORT)

# --- BOT ---
# Pyrogram handle kar lega string ko, tension mat le
bot = Client("master_bot", api_id=int(API_ID) if API_ID else 0, api_hash=API_HASH, bot_token=MASTER_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Bot Live Hai!")

# --- EXECUTION ---
if __name__ == "__main__":
    if not API_ID or not API_HASH or not MASTER_TOKEN:
        print("ERROR: Environment Variables Missing!")
    else:
        Thread(target=run_web, daemon=True).start()
        bot.run()
