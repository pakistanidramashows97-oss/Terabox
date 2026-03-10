🚀 Ultimate TeraBox & DiskWala Downloader Telegram Bot

"Python" (https://img.shields.io/badge/Python-3.10+-blue)
"Pyrogram" (https://img.shields.io/badge/Library-Pyrogram-green)
"License" (https://img.shields.io/badge/License-MIT-yellow)
"Status" (https://img.shields.io/badge/Status-Active-success)

A high-speed multi-site downloader Telegram bot built with Python & Pyrogram.

The bot automatically detects supported links and sends direct MP4 video files to Telegram with fast processing.

Supports TeraBox & DiskWala links with clean UI messages and optimized performance.

---

📸 Bot Preview

Example workflow:

User sends link

https://terabox.com/s/xxxx

Bot response

🔎 Analyzing link...
⚡ Downloading file...
📤 Uploading to Telegram...

🎬 Video sent successfully

---

⚡ Key Features

🚀 Ultra fast downloader
📥 Direct MP4 video sending
🧠 Smart link detection
🌐 Multiple TeraBox domains supported
💾 DiskWala downloader support
⚡ Async processing for maximum speed
📤 Streaming video upload
🐳 Docker ready deployment
☁️ Render / Railway / VPS compatible

---

🌐 Supported Links

TeraBox

https://terabox.com/s/xxxx
https://1024terabox.com/s/xxxx
https://teraboxapp.com/s/xxxx
https://nephobox.com/s/xxxx
https://freeterabox.com/s/xxxx

DiskWala

https://diskwala.com/file/xxxx
https://diskwala.com/d/xxxx
https://diskwala.com/download/xxxx

---

🧠 How It Works

1️⃣ User sends supported link
2️⃣ Bot analyzes the link
3️⃣ Extractor gets direct download URL
4️⃣ Bot downloads or streams the file
5️⃣ Video is uploaded to Telegram

---

📂 Project Structure

Terabox
│
├── main.py
├── config.py
├── handler.py
├── utils.py
│
├── downloader.py
├── uploader.py
│
├── terabox_extractor.py
├── terabox_api.py
├── diskwala_extractor.py
│
├── requirements.txt
├── Dockerfile
└── supported_links.txt

---

⚙️ Installation

Clone repository

git clone https://github.com/pakistanidramashows97-oss/Terabox
cd Terabox

Install dependencies

pip install -r requirements.txt

---

🔑 Environment Variables

Set these variables before running the bot.

API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token

---

▶️ Run Bot

python main.py

---

🐳 Docker Deployment

Build container

docker build -t terabox-bot .

Run container

docker run terabox-bot

---

☁️ Cloud Deployment

You can deploy this bot easily on:

• Render
• Railway
• Koyeb
• VPS

---

⚡ Performance Optimization

This bot uses:

• Async downloading
• Direct streaming upload
• Optimized extractor system

Result → 10x faster than basic downloader bots

---

🛡 Disclaimer

This project is for educational purposes only.

Developers are not responsible for misuse of this software.

---

❤️ Credits

Developed with

Python
Pyrogram
Telegram Bot API

---

⭐ Support The Project

If you like this project please:

⭐ Star the repository
🍴 Fork the project
🚀 Contribute improvements
