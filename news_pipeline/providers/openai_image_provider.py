from .image_provider import ImageProvider
import os, logging
logger = logging.getLogger(__name__)
try:
    import requests
except: requests = None
class OpenAIImageProvider(ImageProvider):
    def generate(self, prompt):
        if requests is None: raise ImportError("requests missing")
        key = os.getenv("OPENAI_API_KEY")
        if not key: raise ValueError("OPENAI_API_KEY missing")
        url = "https://api.openai.com/v1/images/generations"
        resp = requests.post(url, headers={"Authorization":f"Bearer {key}"}, json={"prompt":prompt,"n":1}, timeout=60)
        print("STATUS:", resp.status_code)
        print("HEADERS:", dict(resp.headers))
        print("BODY:", resp.text)
        resp.raise_for_status()
        data = resp.json()
        return data["data"][0]["url"]
