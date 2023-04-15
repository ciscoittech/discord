import os

from dotenv import load_dotenv

load_dotenv()

# Your Discord bot token and OpenAI API key
DISCORD_TOKEN = os.getenv("DISCORD_KEY")
OPENAI_API_KEY = os.getenv("OPEN_AI_KEY")

DB_URL = "sqlite:///discord.db"
