import os
import threading
from flask import Flask
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handler import register_handlers

---------------- FLASK SERVER ----------------

web = Flask(name)

@web.route("/")
def home():
return "Ultimate TeraBox Bot Running"

def run_web():
port = int(os.environ.get("PORT", 8080))
web.run(host="0.0.0.0", port=port)

Start Flask in background thread

threading.Thread(target=run_web).start()

---------------- TELEGRAM BOT ----------------

bot = Client(
"teraboxbot",
api_id=API_ID,
api_hash=API_HASH,
bot_token=BOT_TOKEN
)

Register all handlers

register_handlers(bot)

Run bot

bot.run()
