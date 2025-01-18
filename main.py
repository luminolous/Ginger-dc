import os
import json
import feedparser
from typing import Final
from datetime import datetime
from discord.ext import tasks
from dotenv import load_dotenv
from discord import Intents, Client

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
CHANNEL: Final[int] = int(os.getenv('CHANNEL_ID'))
print(TOKEN)

intents: Intents = Intents.default()
client: Client = Client(intents=intents)



JSON_FILE = "articles.json"

def load_data():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_article_news(title, link):
    data = load_data()
    if not any(article["link"] == link for article in data):
        data.append({"title": title, "link": link})
        save_data(data)
        return 1
    return 0

async def fetch_news():
    rss_url = "https://techcrunch.com/category/artificial-intelligence/feed/"
    feed = feedparser.parse(rss_url)
    messages = []
    for entry in feed.entries[:5]:
        response = add_article_news(entry.title, entry.link)
        if response == 1:
            messages.append(
                f"**Title:** {entry.title}\n**Published:** {entry.published}\n**Link:** {entry.link}"
            )
    return messages

@tasks.loop(minutes=10)
async def post_article_loop():
    channel = client.get_channel(CHANNEL)
    if channel:
        messages = await fetch_news()
        if messages:
            for message in messages:
                await channel.send(message)
        else:
            print("There are no new articles available.")


@client.event
async def on_ready():
    print(f"{client.user} is now running!")
    if not post_article_loop.is_running():
        post_article_loop.start()

def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()