import os

class Config(object): 
    # Telegram Vars
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    ADMINS = set(int(x) for x in os.environ.get("ADMINS", "").split())
    
    #Bot Stuff
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    if BOT_USERNAME.startswith("@"):
        BOT_USERNAME = BOT_USERNAME[1:]
    # Heroku API Vars
    # Copy Paste the below vars and rename it with correct
    # numbers if you need to add more apps
    HRK_API = os.environ.get("HRK_API")
    # Heroku APP Vars
    HRK_APP_NAME = os.environ.get("HRK_APP_NAME", 'mybots')
