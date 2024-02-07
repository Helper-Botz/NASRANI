import os
from PIL import Image
from pyrogram import Client,filters 
from pyrogram.types import (InlineKeyboardButton,  InlineKeyboardMarkup)

from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

import os
import shutil
from pyrogram import Client, filters, enums
from telegraph import upload_file
from plugins.helpers.get_file_id import get_file_id
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup




BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", 12345))

API_HASH = os.environ.get("API_HASH", "")
app = Client(
        "pdf",
        bot_token=BOT_TOKEN,api_hash=API_HASH,
            api_id=API_ID
    )


LIST = {}

TMP_DOWNLOAD_DIRECTORY = "./DOWNLOADS/"


@Client.on_message(filters.command("imgpdf") & filters.photo)
async def pdf(client,message):
 
    if not isinstance(LIST.get(message.from_user.id), list):
        LIST[message.from_user.id] = []  
 
    file_id = str(message.photo.file_id)
    ms = await message.reply_text("Converting to PDF ......")
    file = await client.download_media(file_id)
 
    image = Image.open(file)
    img = image.convert('RGB')
    LIST[message.from_user.id].append(img)
    await ms.edit(f"{len(LIST[message.from_user.id])} image   Successful created PDF if you want add more image Send me One by one\n\n **if done click here 👉 /convert** ")
 

@Client.on_message(filters.command(['convert']))
async def done(client,message):
    chat_id = message.chat.id
    images = LIST.get(message.from_user.id)
#    koshik = await message.reply_text("**Processing...😪**")
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("Reply to a supported media file")
        return
    file_info = get_file_id(replied)
    if not file_info:
        await message.reply_text("Not supported!")
        return
    _t = os.path.join(
        TMP_DOWNLOAD_DIRECTORY,
        str(replied.id)
    )
    if not os.path.isdir(_t):
        os.makedirs(_t)
    _t += "/"
    download_location = await replied.download(
        _t
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await koshik.edit_text(message, text=document)
    if isinstance(images, list):
        del LIST[message.from_user.id]
    if not images:
        await message.reply_text( "No image !!")
        return

    path = f"{message.from_user.id}" + ".pdf"
    images[0].save(path, save_all = True, append_images = images[1:])
 
    await client.send_document(message.from_user.id, open(path, "rb"), caption = f"<b>Link :-</b> <code>https://telegra.ph{response[0]}</code>\n\n<b>")
    os.remove(path)
