import requests
from requests import get 
from pyrogram import filters, Client
from pyrogram.types import InputMediaPhoto


import os
import requests
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp





     




@Client.on_message(filters.command(["wall"]))
async def wall(client, message):
    
    user_id = message.from_user.id
#    if user_id in configs.owner_id:
    chat_id = message.chat.id
    r = requests.get(url = 'https://api.waifu.pics/sfw/neko')
    data = r.json()
    print(data)
    print(type(data))
    await message.reply(data['url'])
     





@Client.on_message(filters.chat(-1001203428484) & filters.command('image'))
# @Client.on_message(filters.command(["image"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def pinterest(bot, message):
     chat_id = message.chat.id

     try:
       query= message.text.split(None,1)[1]
     except:
         return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

     images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()

     media_group = []
     count = 0

     msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ ᴘɪɴᴛᴇʀᴇᴛs...")
     for url in images["images"][:6]:
                  
          media_group.append(InputMediaPhoto(media=url))
          count += 1
          await msg.edit(f"=> ᴏᴡᴏ sᴄʀᴀᴘᴇᴅ ɪᴍᴀɢᴇs {count}")

     try:
        
        await bot.send_media_group(
                chat_id=chat_id, 
                media=media_group,
                reply_to_message_id=message.id)
        return await msg.delete()

     except Exception as e:
           await msg.delete()
           return await message.reply(f"ᴇʀʀᴏʀ : {e}")



@Client.on_message(filters.command("write"))
async def handwrite(bot, message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "Please wait...,\n\nWriting your text...")
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘
✨ ᴡʀɪᴛᴛᴇɴ ʙʏ : [˹ 𝗠ᴇʟᴀɴɪᴀ ✘ 𝗥𝙾𝙱𝙾 ˼](https://t.me/{temp.U_NAME})
🥀 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention}
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption)
