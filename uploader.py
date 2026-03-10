async def upload_files(client, message, files):

total = len(files)

for index, file in enumerate(files, start=1):

    await message.reply_text(
        f"📂 Uploading file {index}/{total}\n\n🎬 {file['name']}"
    )

    await message.reply_video(
        video=file["url"],
        caption=f"🎬 {file['name']}\n📦 Size: {file['size']}",
        supports_streaming=True
    )
