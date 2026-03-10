from pyrogram import filters
from utils import detect_link
from terabox_extractor import extract_terabox
from diskwala_extractor import extract_diskwala
from uploader import upload_video

def register_handlers(app):

    @app.on_message(filters.private)
    async def downloader(client, message):

        link_type = detect_link(message.text)

        if not link_type:
            return

        status = await message.reply("🔎 Analyzing link...")

        if link_type == "terabox":
            data = await extract_terabox(message.text)

        if link_type == "diskwala":
            data = await extract_diskwala(message.text)

        await status.edit("⚡ Downloading...")

        await upload_video(client, message, data)
