from .telegram_publisher import TelegramPublisher
import os, logging
try:
    import requests
except ImportError:
    requests = None
logger = logging.getLogger(__name__)
class TelegramBotPublisher(TelegramPublisher):
    def publish(self, post):
        token = os.getenv("BOT_TOKEN")
        chat = os.getenv("TARGET_CHAT")
        if post.get("image"):
            r = requests.post(f"https://api.telegram.org/bot{token}/sendPhoto", data={"chat_id":chat,"photo":post["image"],"caption":post.get("caption","")})
        else:
            r = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={"chat_id":chat,"text":post.get("caption","")})
        r.raise_for_status()
        return r.json()
