import os

from dotenv import load_dotenv

load_dotenv()

db_name = "discord"
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_port = "5432"


# Your Discord bot token and OpenAI API key
DISCORD_TOKEN = os.getenv("DISCORD_KEY")
OPENAI_API_KEY = os.getenv("OPEN_AI_KEY")



# DB_URL = "sqlite:///discord.db"
PG_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
