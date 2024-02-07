import imghdr, os
from asyncio import gather
from traceback import format_exc
from pyrogram import filters, Client, enums
from pyrogram.types import *
from pyrogram.errors import *
# from utils.files import *
# from utils.stickerset import *
from datetime import datetime    


# © BugHunterCodeLabs ™
# © bughunter0
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import os , glob
from os import error
import logging
import pyrogram
import time
import math
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document
import asyncio
import os
import math
import time
import requests
from pyrogram import Client, filters


##########       STREAM
import logging
# from urllib.parse import quote_plus
# from plugins.helpers.file_properties import get_name, get_hash, get_media_file_size

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
##########       STREAM


bughunter0 = Client(
    "Sticker-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

MAX_STICKERS = (120)  # would be better if we could fetch this limit directly from telegram
SUPPORTED_TYPES = ["jpeg", "png", "webp", "gif", "mp4"]
    


START_TIME = datetime.utcnow()


START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()


TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

START_STRING = """ Hi {}, I'm Sticker Bot. 

I can Provide all Kind of Sticker Options Here """


JOIN_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/nasrani_update')
        ]]
    )

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

#=====================================================
BOT_START_TIME = time.time()
#=====================================================


async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
   




@Client.on_message(filters.command("pong"))
async def pong(_, message):
    start_t = time.time()  
    avr = await message.reply_text("•••")  
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = time.strftime("%Hh | %Mm | %Ss", time.gmtime(time.time() - BOT_START_TIME))   
    await avr.edit(f"ᴄᴜʀʀᴇɴᴛ ʙᴏᴛ sᴛᴀᴛᴜs\n\n‹› ᴘᴏɴɢ! : {time_taken_s:.3f} ms\n‹› ʙᴏᴛ ᴜᴘᴛɪɴᴇ : {uptime}")
    await asyncio.sleep(10)
    await avr.delete()

@Client.on_message(filters.chat(-1001203428484) & filters.command('start_sticker'))
async def start_sticker(bot, update):
    text = START_STRING.format(update.from_user.mention)
    reply_markup = JOIN_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )


@Client.on_message(filters.chat(-1001203428484) & filters.command('ping'))
async def ping(bot, message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    start_t = time.time()
    rm = await message.reply_text("Checking")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(
        "Pong!\n"
        f"{time_taken_s:.3f} ms\n\n"
        "🤖 Bot status:\n"
        f"• **Uptime:** `{uptime}`\n"
        f"• **Start time:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.chat(-1001203428484) & filters.command('alive'))
async def alive(bot, message):
    await message.reply_document(f"BQACAgQAAx0CbSitBQACETJkw9__TNjSs50hmpGPXnxovk6eTAACJw4AAltmEFFvEc8DS7Kipx4E")
    




@Client.on_message(filters.chat(-1001203428484) & filters.command('getsticker'))
async def getstickerasfile(bot, message):      
    try :     
                     
        tx = await message.reply_text("Downloading...")
        file_path = DOWNLOAD_LOCATION + f"{message.chat.id}.WEBM"
        await message.reply_to_message.download(file_path)   
        await tx.edit("Downloaded")
        await tx.edit("Uploading...")
        start = time.time()
        await message.reply_document(file_path,caption="©NASRANI_UPDATE")
        await tx.delete()   
        os.remove(file_path)
    except Exception as error:
        print(error)    





@Client.on_message(filters.chat(-1001203428484) & filters.command('clearcache'))
async def clearcache(bot, message):   
    # Found some Files showing error while Uploading, So a method to Remove it !!  
    txt = await message.reply_text("Checking Cache")
    await txt.edit("Clearing cache")
    dir = DOWNLOAD_LOCATION
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist :
           i =1
           os.remove(f)
           i=i+1
    await txt.edit("Cleared "+ str(i) + "File") 
    await txt.delete()
    

@Client.on_message(filters.chat(-1001203428484) & filters.command('stickerid'))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply_text(
#       chat_id=message.chat.id,
       text=f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")



@Client.on_message(filters.chat(-1001203428484) & filters.command('find'))
async def find(bot, message):  
    txt = await message.reply_text("Validating Sticker ID")
    stickerid = message.reply_to_message.text
    chat_id = message.chat.id
    await txt.delete()
    await bot.send_sticker(chat_id,f"{stickerid}")
   



@Client.on_message(filters.chat(-1001203428484) & filters.command('doc'))
async def document(bot, message):
    videoid= message.reply_to_message.text
    documentid= message.reply_to_message.text
    chat_id = message.chat.id
    buttons = [[
        InlineKeyboardButton('🖥️𝐂𝐡𝐫𝐨𝐦𝐞 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝🖥️', callback_data=f'generate_stream_link:{videoid}')
        
    ]]            
    kf = await bot.send_cached_media(
        chat_id=chat_id,
        file_id=f"{documentid or videoid}",
        parse_mode=enums.ParseMode.HTML,                                
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    await asyncio.sleep(120)
    await k.delete()
    
    videoid= message.reply_to_message.text
    documentid= message.reply_to_message.text
    chat_id = message.chat.id
#    await txt.delete()
#    m = await message.reply_text("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝 𝚈𝚘𝚞𝚛 𝙵𝚒𝚕𝚎. ♻**......\n\n[░░░░░░░░░░] 00%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇░░░░░░░░] 20%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇▇▇░░░░░░] 40%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇▇▇▇░░░░░] 50%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
#    await m.edit("**♻ 𝙲𝚘𝚗𝚟𝚎𝚛𝚝  𝙵𝚒𝚕𝚎... ♻**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
#    await m.edit("📤Uploading....")
#    await m.edit("📤Uploading.....")
    fileName = {quote_plus(get_name(videoid))}
    lazy_stream = f"{URL}watch/{str(videoid.id)}/{quote_plus(get_name(videoid))}?hash={get_hash(videoid)}"
    lazy_download = f"{URL}{str(videoid.id)}/{quote_plus(get_name(videoid))}?hash={get_hash(videoid)}"

    await client.send_message(
        chat_id=chat_id,
        text=f"•• ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ꜰᴏʀ ɪᴅ #{user_id} \n•• ᴜꜱᴇʀɴᴀᴍᴇ : {username} \n\n•• ᖴᎥᒪᗴ Nᗩᗰᗴ : {kf}",
        quote=True,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚀 Fast Download 🚀", url=lazy_download),  # we download Link
                                              InlineKeyboardButton('🖥️ Watch online 🖥️', url=lazy_stream)]]))  # web stream Link
        



@Client.on_message(filters.chat(-1001203428484) & filters.command('file'))
async def documentid(bot, message):   
    if message.reply_to_message.document or message.reply_to_message.video:
       await message.reply_text(
#       chat_id=message.chat.id,
       text=f"**Sticker ID is**  \n `{message.reply_to_message.document or message.reply_to_message.video.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.document or message.reply_to_message.video.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")







@Client.on_message(filters.chat(-1001203428484) & filters.command('findsticker'))
async def findsticker(bot, message):  
    try:
        
        txt = await message.reply_text("Validating Sticker ID")
        stickerid = str(message.reply_to_message.text)
        chat_id = str(message.chat.id)
        await txt.delete()
        await bot.send_sticker(chat_id,f"{stickerid}")
     
    except Exception as error:
        print(error)
        txt = await message.reply_text("Not a Valid File ID")

      






@Client.on_message(filters.chat(-1001203428484) & filters.command('get_sticker'))
async def sticker_image(_, message: Message):
    r = message.reply_to_message

    if not r:
        return await message.reply("Reply to a sticker.")

    if not r.sticker:
        return await message.reply("Reply to a sticker.")

    m = await message.reply("Sending..")
    f = await r.download(f"{r.sticker.file_unique_id}.png")
    k = await message.reply_photo(f)
    s = await message.reply_document(f)
    

    await m.delete()
    os.remove(f)
