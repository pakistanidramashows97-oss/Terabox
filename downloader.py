import os
import uuid
import requests
from config import DOWNLOAD_DIR

async def download_video(link):

    # Demo direct link
    video_url = "DIRECT_VIDEO_LINK"

    file_name = str(uuid.uuid4()) + ".mp4"
    file_path = os.path.join(DOWNLOAD_DIR, file_name)

    r = requests.get(video_url)

    with open(file_path, "wb") as f:
        f.write(r.content)

    size = str(round(os.path.getsize(file_path)/1024/1024,2)) + " MB"

    return file_path, file_name, size
