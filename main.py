from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response, start_book, update_progress, get_progress

#load the .env file
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


# Create a new Client instance
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)





async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('message was empty because intents were not enabled')
        return
    if is_private := user_message[0] == "?":
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(f"Error: {e}")



# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return

    content = message.content
    if content.startswith('!startBook'):
        _, book_id, total_pages = content.split()
        response = start_book(str(message.author.id), book_id, int(total_pages))
        await message.channel.send(response)
    elif content.startswith('!updateProgress'):
        _, book_id, current_page = content.split()
        response = update_progress(str(message.author.id), book_id, int(current_page))
        await message.channel.send(response)
    elif content.startswith('!checkProgress'):
        _, book_id = content.split()
        response = get_progress(str(message.author.id), book_id)
        await message.channel.send(response)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()