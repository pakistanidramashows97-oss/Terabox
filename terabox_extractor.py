import requests

async def extract_terabox(link):

    api = "https://terabox-extractor-api.vercel.app/api"

    r = requests.get(api, params={"url": link})

    data = r.json()

    return {
        "url": data["download_url"],
        "name": data["file_name"],
        "size": data["size"]
    }
