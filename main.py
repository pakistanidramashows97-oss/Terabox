import os
import threading
from flask import Flask
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handler import register_handlers

web = Flask(__name__)

@web.route("/")
def home():
    return "Ultimate TeraBox Bot Running"

def run():
    port = int(os.environ.get("PORT", 8080))
    web.run(host="0.0.0.0", port=port)

threading.Thread(target=run).start()

bot = Client(
    "teraboxbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_handlers(bot)

bot.run()
