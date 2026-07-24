import sys, os, json, logging
from dotenv import load_dotenv
load_dotenv()
from telethon import TelegramClient, events
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
client = TelegramClient('session', int(os.getenv("API_ID","0")), os.getenv("API_HASH",""))
channels_raw = json.load(open('channels.json')) if os.path.exists('channels.json') else []

async def main():
    await client.start()
    me = await client.get_me()
    print(f"ACCOUNT: id={me.id} username={me.username} first_name={me.first_name}")
    resolved = []
    for ch in channels_raw:
        try:
            ent = await client.get_entity(ch)
            print(f"CHANNEL RESOLVED: id={ent.id} title={ent.title} username={ent.username}")
            resolved.append(ent)
        except Exception as e:
            print(f"CHANNEL RESOLVE FAILED: {ch} -> {e}")
            await client.disconnect()
            sys.exit(1)
    @client.on(events.NewMessage(chats=resolved))
    async def handler(event):
        print(f"MESSAGE: chat={event.chat.title} id={event.message.id} text={event.message.text[:100]}")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
