import os
import requests
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client("downloader", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def get_video(link):
    
    apis = [
        f"https://teraboxdownloader.nepcoderdevs.workers.dev/?url={link}",
        f"https://terabox-api.vercel.app/api?url={link}"
    ]

    for api in apis:
        try:
            r = requests.get(api, timeout=20)
            if r.status_code == 200:
                data = r.json()

                if "download" in data:
                    return data["download"]

                if "download_link" in data:
                    return data["download_link"]
        except:
            pass

    return None


@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Send Terabox or DiskWala link")


@bot.on_message(filters.text)
async def download(client, message):

    link = message.text.strip()

    if "terabox" not in link and "1024tera" not in link and "diskwala" not in link:
        await message.reply_text("❌ Send valid Terabox / DiskWala link")
        return

    msg = await message.reply_text("🔎 Getting video link...")

    video = get_video(link)

    if not video:
        await msg.edit("❌ Could not fetch video. Try another link.")
        return

    await msg.edit("📤 Uploading video...")

    await message.reply_video(video)

    await msg.delete()


bot.run()
