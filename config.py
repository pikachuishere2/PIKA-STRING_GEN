from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", MONGO_DB_URL=mongodb+srv://vivek:1234567890@cluster0.c48d8ih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)

OWNER_ID = int(getenv("OWNER_ID", 7374531519)) 
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+f37Lk-OMx4tmOGJl")
