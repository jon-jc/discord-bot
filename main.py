from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#load the .env file
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


# Create a new Client instance
intents: Intents = Intents.default()
intents.message_content = True #N0QA
client: Client = Client(intents=intents)