import discord
import openai
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DISCORD_TOKEN, OPENAI_API_KEY, DB_URL
from models import Entry, Base

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

# Set up the SQLAlchemy engine and session
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Create a new Discord client instance with the necessary intents
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


# Define an event for when the bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} ({client.user.id})")


# Define an event for when a message is sent in the server
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Generate a response using OpenAI's Chat API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.content},
        ],
        max_tokens=100,
        temperature=0.5,
    )

    # Send the response back to the Discord server
    bot_response = response.choices[0].message['content']
    await message.channel.send(bot_response)

    # Store the entry in the PostgreSQL database using SQLAlchemy
    entry = Entry(user_id=message.author.id, user_message=message.content, bot_response=bot_response)
    session.add(entry)
    session.commit()


# Start the bot
client.run(DISCORD_TOKEN)
