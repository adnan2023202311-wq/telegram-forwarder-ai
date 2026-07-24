import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass
from news_pipeline.publishers.telegram_bot_publisher import TelegramBotPublisher
pub = TelegramBotPublisher()
res = pub.publish({"caption":"✅ TEST MESSAGE\nTelegram publishing works.","image":None})
print("PUBLISHED:", res)
