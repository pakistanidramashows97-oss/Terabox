import requests

async def extract_folder(link):

api = "https://terabox-extractor-api.vercel.app/api"

r = requests.get(api, params={"url": link})

data = r.json()

files = []

for file in data["files"]:
    files.append({
        "name": file["name"],
        "url": file["download_url"],
        "size": file["size"]
    })

return files
