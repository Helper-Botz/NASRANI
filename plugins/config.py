import re
import os
from os import environ
from dotenv import load_dotenv
load_dotenv()

id_pattern = re.compile(r'^.\d+$')




# open ai
import re
from os import getenv, environ



id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default




HRK_APP_NAME = environ.get('HRK_APP_NAME', 'mybots')
HRK_API = os.environ.get("HRK_API")
ADMINS = int(os.environ.get("ADMINS"))
GIT_TOKEN = os.environ.get("GIT_TOKEN")

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
ADMINS = int(environ.get("ADMINS", ""))
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), True)
#open ai

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
ADMINS = int(environ.get("ADMINS", ""))          
CAPTION = environ.get("CAPTION", "")

# for thumbnail ( back end is MrMKN brain 😉)
DOWNLOAD_LOCATION = "./DOWNLOADS"
RemoveBG_API = os.environ.get("RemoveBG_API", "")

# mdisk
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MDISK_API = os.environ.get("MDISK_API")
MDISK_CHANNEL = list(int(i.strip()) for i in os.environ.get("MDISK_CHANNEL").split(" ")) if os.environ.get("CHANNEL_ID") else []
FORWARD_MESSAGE = bool(os.environ.get("FORWARD_MESSAGE"))
ADMINS = list(int(i.strip()) for i in os.environ.get("ADMINS").split(",")) if os.environ.get("ADMINS") else []
SOURCE_CODE = "💕SHARE AND SUPPORT💕"
CHANNELS = bool(os.environ.get("CHANNELS"))


# attach


class Config(object):
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  #CHANNEL_USERNAME without '@'
  CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", "bigmoviesworld")





