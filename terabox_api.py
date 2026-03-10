import requests

async def get_download_link(link):

    api = "https://terabox-extractor-api.vercel.app/api"

    r = requests.get(api, params={"url": link})

    data = r.json()

    return data
