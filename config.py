import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", 1736204))
    API_HASH = os.environ.get("API_HASH" "890d40e0f91a4de32dec2965444b2cbe")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6159823074:AAG-lCFVF6-7UfJyhKJOev5_RF-EUkwmXds")
    OWNER_ID = int(os.environ.get("OWNER_ID", 1058015838))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", None)
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Testing:Testing@cluster0.fkelfqj.mongodb.net/?retryWrites=true&w=majority")
