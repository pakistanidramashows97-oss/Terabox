async def upload(client, message, data):

    await message.reply_video(
        video=data["url"],
        caption=f"🎬 {data['name']}\n📦 Size: {data['size']}",
        supports_streaming=True
    )
