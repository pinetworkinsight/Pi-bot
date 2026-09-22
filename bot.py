import os, asyncio, feedparser, requests, threading
from telegram import Bot
import datetime
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Pi Bot is Alive!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web, daemon=True).start()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

async def main():
    bot = Bot(token=BOT_TOKEN)
    while True:
        try:
            feed = feedparser.parse("https://www.pinetworknews.com/feed/")
            if feed.entries:
                news = feed.entries[0]
                text = f"🚨 PI NETWORK UPDATE\n\n{news.title}\n\n{news.link}"
                await bot.send_message(chat_id=CHANNEL_ID, text=text)
        except Exception as e:
            print(e)
        await asyncio.sleep(3600) # 1 hour

if __name__ == "__main__":
    asyncio.run(main())
