from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from news import *
from add_articles import *

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
CHANNEL: Final[str] = os.getenv('DISCORD_CHANNEL')
print(TOKEN)

intents: Intents = Intents.default()
client: Client = Client(intents=intents)

async def post_article():
    channel = client.get_channel(CHANNEL)
    if channel:
        response = news_post()
        await channel.send(response)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()