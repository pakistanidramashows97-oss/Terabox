import os
import requests
from pyrogram import Client, filters
from keep_alive import keep_alive

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client(
    "downloader_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "👋 Send Terabox or DiskWala link\n\nI will send the MP4 video."
    )

@bot.on_message(filters.text)
async def downloader(client, message):

    link = message.text

    if not any(x in link for x in ["terabox", "1024tera", "diskwala"]):
        await message.reply_text("❌ Send valid Terabox / DiskWala link")
        return

    msg = await message.reply_text("🔎 Fetching video...")

    api = f"https://terabox-dl-api.vercel.app/api?url={link}"

    try:
        data = requests.get(api).json()

        video_url = data["download_link"]
        title = data.get("title", "Video")

        await msg.edit("📤 Uploading video...")

        await message.reply_video(
            video_url,
            caption=f"🎬 {title}"
        )

        await msg.delete()

    except Exception as e:
        await msg.edit("❌ Failed to fetch video")

keep_alive()

bot.run()
