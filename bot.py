from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "MovieFilterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def test(client, message):
    print(message.text)

app.run()
