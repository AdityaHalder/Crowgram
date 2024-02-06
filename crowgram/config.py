from dotenv import load_dotenv
from os import getenv

load_dotenv()

API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING_SESSION = getenv("STRING_SESSION", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", None))

