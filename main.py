import os
import requests
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client("terabox_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def get_video(link):

    apis = [
        f"https://teraboxdownloader.nepcoderdevs.workers.dev/?url={link}",
        f"https://terabox-api.vercel.app/api?url={link}",
        f"https://api.teraboxdownloader.xyz/?url={link}",
        f"https://terabox-dl-api.vercel.app/api?url={link}",
        f"https://api.nepcoderdevs.workers.dev/terabox?url={link}"
    ]

    for api in apis:
        try:
            r = requests.get(api, timeout=20)
            if r.status_code == 200:
                data = r.json()

                video = (
                    data.get("download") or
                    data.get("download_link") or
                    data.get("video")
                )

                if video:
                    return video
        except:
            continue

    return None


@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Send Terabox or DiskWala link")


@bot.on_message(filters.text)
async def download(client, message):

    link = message.text.strip()

    if not any(x in link for x in ["terabox","1024tera","diskwala"]):
        await message.reply_text("Send valid Terabox / DiskWala link")
        return

    msg = await message.reply_text("Fetching video...")

    video = get_video(link)

    if not video:
        await msg.edit("Link temporarily not working. Try another link.")
        return

    await msg.edit("Uploading MP4...")

    await message.reply_video(video)

    await msg.delete()


bot.run()
