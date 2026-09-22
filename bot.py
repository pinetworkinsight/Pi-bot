import os, asyncio, feedparser, requests
from telegram import Bot
import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
async def main():
    bot = Bot(token=BOT_TOKEN)
    while True:
        try:
            feed = feedparser.parse("https://news.google.com/rss/search?q=Pi+Network&hl=en-US&gl=US&ceid=US:en")
            if feed.entries:
                news = feed.entries[0]
                text = f"🚨 PI NETWORK UPDATE 🚨\n\n📰 {news.title}\n\n{news.link}\n\n#{datetime.datetime.now().strftime('%Y-%m-%d')} #PiNetwork"
                await bot.send_message(chat_id=CHANNEL_ID, text=text)
        except Exception as e:
            print(e)
        await asyncio.sleep(3600) # 1 hour

if __name__ == "__main__":
    asyncio.run(main())
