import requests

async def extract_diskwala(link):

    api = "https://diskwala-api.vercel.app/api"

    r = requests.get(api, params={"url": link})

    return r.json()
