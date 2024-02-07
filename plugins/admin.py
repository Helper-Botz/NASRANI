import os
import time
import math
import json
import string
import random
import traceback
import asyncio
import datetime
import motor.motor_asyncio
import aiofiles
from io import BytesIO
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
# from plugins.helpers.vars import DEFAULT_LANGUAGE, ADMINS, DATABASE_URL
# from plugins.helpers.vars import DEFAULT_LANGUAGE, ADMINS, DATABASE

ADMINS = int(os.environ.get("ADMINS"))
DATABASE = os.environ.get("DATABASE_URL")
DEFAULT_LANGUAGE = os.environ.get("DEFAULT_LANGUAGE", "ml")
EN_LANGUAGE = os.environ.get("EN_LANGUAGE", "en")
HI_LANGUAGE = os.environ.get("HI_LANGUAGE", "hi")
TM_LANGUAGE = os.environ.get("TM_LANGUAGE", "ta")



class Katabase:
    def __init__(self, uri, database_name="Translator-Bot"):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.cache = {}
    
    def new_user(self, id):
        return {"id": id, "language": DEFAULT_LANGUAGE}
    
    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)
    
    async def get_user(self, id):
        user = self.cache.get(id)
        if user is not None:
            return user
        
        user = await self.col.find_one({"id": int(id)})
        self.cache[id] = user
        return user
    
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return True if user else False
    
    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count
    
    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users
    
    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})
    
    async def get_lang(self, id):
        user = await self.col.find_one({'id': int(id)})
        if user:
            return user.get("language", DEFAULT_LANGUAGE)

    async def en_lang(self, id):
        user = await self.col.find_one({'id': int(id)})
        if user:
            return user.get("language", EN_LANGUAGE)


    async def hi_lang(self, id):
        user = await self.col.find_one({'id': int(id)})
        if user:
            return user.get("language", HI_LANGUAGE)


    async def tm_lang(self, id):
        user = await self.col.find_one({'id': int(id)})
        if user:
            return user.get("language", TM_LANGUAGE)
  


    async def update_lang(self, id, language):
        await self.col.update_one(
            {"id": id}, {"$set": {"language": language}}
        )


async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"


