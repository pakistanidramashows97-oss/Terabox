from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Start Image

START_IMAGE = "https://i.ibb.co/WpKRVMKy/7168219724-28094.jpg"

Start Message

START_TEXT = """
𝑾𝒆𝒍𝒄𝒐𝒎𝒆, {𝑨𝒏𝒖𝒋}.

🌟 𝑰 𝒂𝒎 𝒂 𝑻𝒆𝒓𝒂𝑩𝒐𝒙 𝒐𝒓 𝑫𝒊𝒔𝒌𝒘𝒂𝒍𝒂 𝑳𝒊𝒏𝒌 𝒕𝒐 𝑽𝒊𝒅𝒆𝒐 𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅𝒆𝒓 𝑩𝒐𝒕.

𝑺𝒆𝒏𝒅 𝒎𝒆 𝒂𝒏𝒚 𝑻𝒆𝒓𝒂𝑩𝒐𝒙 𝒐𝒓 𝑫𝒊𝒔𝒌𝒘𝒂𝒍𝒂 𝒍𝒊𝒏𝒌 𝒂𝒏𝒅 𝑰 𝒘𝒊𝒍𝒍 𝒅𝒐𝒘𝒏𝒍𝒐𝒂𝒅 𝒊𝒕 𝒘𝒊𝒕𝒉𝒊𝒏 𝒂 𝒇𝒆𝒘 𝒔𝒆𝒄𝒐𝒏𝒅𝒔 𝒂𝒏𝒅 𝒔𝒆𝒏𝒅 𝒊𝒕 𝒕𝒐 𝒚𝒐𝒖.✨

👥 𝑹𝒆𝒇𝒆𝒓 𝒚𝒐𝒖𝒓 𝑭𝒓𝒊𝒆𝒏𝒅𝒔 𝒂𝒏𝒅 𝑮𝒆𝒕 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑷𝒍𝒂𝒏 Free » /refer
"""

Start Command

@Client.on_message(filters.command("start"))
async def start_command(client, message):

name = message.from_user.first_name

buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📢 Join Channel", url="https://t.me/arafta_hindi_dubbed_webseries")
        ],
        [
            InlineKeyboardButton("👥 Refer Friends", callback_data="refer"),
            InlineKeyboardButton("❓ Help", callback_data="help")
        ]
    ]
)

await message.reply_photo(
    photo=START_IMAGE,
    caption=START_TEXT.format(name=name),
    reply_markup=buttons
)

Refer Button

@Client.on_callback_query(filters.regex("refer"))
async def refer_button(client, callback_query):

user_id = callback_query.from_user.id
bot_username = (await client.get_me()).username

link = f"https://t.me/{terabox_down_anuj_bot}?start=ref_{7521421400}"

await callback_query.message.reply_text(
    f"👥 Your Referral Link:\n\n{http://t.me/arafta_hindi_dubbed_webseries}\n\nShare this link with friends and earn rewards!"
)

Help Button

@Client.on_callback_query(filters.regex("help"))
async def help_button(client, callback_query):

await callback_query.message.reply_text(
    "📥 Send any TeraBox or Diskwala link.\n\n"
    "The bot will download the video and send it to you automatically."

Help Button
@Client.on_callback_query(filters.regex("help")) async def help_button(client, callback_query):
await callback_query.message.reply_text(
    "📥 Send any TeraBox or Diskwala link.\n\n"
    "The bot will download the video and send it to you automatically."
)
)
