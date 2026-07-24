import os, json, logging
from dotenv import load_dotenv
load_dotenv()
from telethon import TelegramClient, events
from news_pipeline.pipeline import NewsPipeline
from news_pipeline.publishers.telegram_bot_publisher import TelegramBotPublisher
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
client = TelegramClient('session', int(os.getenv("API_ID","0")), os.getenv("API_HASH",""))
channels = json.load(open('channels.json')) if os.path.exists('channels.json') else []
logger.info("Listening on %s", channels)

@client.on(events.NewMessage(chats=channels))
async def on_new(event):
    logger.info("Received message %d from %s", event.message.id, event.chat.title if event.chat else "Unknown")
    try:
        p = NewsPipeline()
        logger.info("AI request started")
        result = await p.run(event.message.text or "")
        logger.info("AI response: %s", result)
        pub = TelegramBotPublisher()
        target = os.getenv("TELEGRAM_TARGET_CHANNEL")
        payload = result.get("payload",{})
        logger.info("Publishing to %s", target)
        res = pub.publish({"caption": payload.get("caption",""), "image": payload.get("image")})
        logger.info("Published: %s", res)
    except Exception as e:
        logger.error("Pipeline failed: %s", e)

with client:
    client.run_until_disconnected()
