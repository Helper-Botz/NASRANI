# (c) @KoshikKumar17
import os
import requests
import pyrogram
import json
from info import LOG_CHANNEL
from pyrogram import Client as Koshik
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('✨𝐔𝐩𝐝𝐚𝐭𝐞𝐝 𝐛𝐲✨', url='https://t.me/nasrani_update')]])
A = """{} with user id:- {} used /git command."""

import logging
import os
import requests
from pyrogram import Client, filters
from info import SUPPORT_CHAT_ID

START_MESSAGE = """
<b>𝐍𝐚𝐦𝐞 : </b> <i>{qw.get("name")}</i>

<b>𝐅𝐮𝐥𝐥 𝐍𝐚𝐦𝐞 : </b> <i>{qw.get("full_name")}</i>

<b>𝐋𝐢𝐧𝐤 :</b> {qw.get("html_url")}

<b>𝐅𝐨𝐫𝐤 𝐂𝐨𝐮𝐧𝐭 : </b> <i>{qw.get("forks_count")}</i>

<b>𝐎𝐩𝐞𝐧 𝐈𝐬𝐬𝐮𝐞𝐬 : </b> <i>{qw.get("open_issues")}</i>

𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬 : <a href='https://github.com/search?q={}+language%3APython&type=repositories&l=Python&s=updated&o=desc'>{}</a>

"""

# (c) @KoshikKumar17
import os
import requests
import pyrogram
import json
from info import LOG_CHANNEL
from pyrogram import Client as Koshik
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('✨ Made By ✨', url='https://t.me/nasrani_update')]])
A = """{} with user id:- {} used /git command."""


# @Client.on_message(filters.command("react"))
# async def twing(client, message):
#    try:
#    message_id = message.text
#    await client.send_reaction(chat_id, message_id, "🥰")
#    except:
#        return


# @Client.on_message(filters.private)
# async def reaction(client, message):
#    await client.send_reaction(chat_id, message_id, "🔥")




@Client.on_message(filters.chat(-1001203428484) & filters.text & filters.command('github'))
async def getgithub(bot, message):
    if len(message.command) != 2:
        await message.reply_text("/github Username \n\n Like:- `/github hkrrish`", quote=True)
        return
    await message.reply_chat_action(enums.ChatAction.TYPING)
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    un = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{un}'
    request = requests.get(URL)
    result = request.json()
    username = result['login']
    url = result['html_url']
    name = result['name']
    company = result['company']
    bio = result['bio']
    created_at = result['created_at']
    avatar_url = result['avatar_url']
    blog = result['blog']
    location = result['location']
    repositories = result['public_repos']
    followers = result['followers']
    following = result['following']
    capy = f"""
𝐈𝐧𝐟𝐨 𝐨𝐟 `{name}`

𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : `{username}`

𝐁𝐢𝐨 : `{bio}`

𝐏𝐫𝐨𝐟𝐢𝐥𝐞 𝐋𝐢𝐧𝐤 : [Click Here]({url})

𝐂𝐨𝐦𝐩𝐚𝐧𝐲 : `{company}`

𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐨𝐧 : `{created_at}`

𝐑𝐞𝐩𝐨𝐬𝐢𝐭𝐨𝐫𝐢𝐞𝐬 : `{repositories}`

𝐁𝐥𝐨𝐠 : `{blog}`

𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧 : `{location}`

𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : `{followers}`

𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : `{following}`
"""
    await message.reply_photo(photo=avatar_url, caption=capy, reply_markup=BUTTONS)
    await bot.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
    await k.delete()
        





@Client.on_message(filters.chat(-1001203428484) & filters.text & filters.command('repo'))

# @Client.on_message(filters.command('repo') & filters.chat (SUPPORT_CHAT_ID))
async def git(Kashmira, message):
    pablo = await message.reply_text("Processing...")
    args = message.text.split(None, 1)[1]
    if len(message.command) == 1:
        await pablo.edit("No input found")
        return
    r = requests.get("https://api.github.com/search/repositories", params={"q": args})
    lool = r.json()
    if lool.get("total_count") == 0:
        await pablo.edit("File not found")
        return
    else:
        lol = lool.get("items")
        qw = lol[0]
#        txt = f"""
# <b>Name :</b> <i>{qw.get("name")}</i>

# <b>Full Name :</b> <i>{qw.get("full_name")}</i>

# <b>Link :</b> {qw.get("html_url")}

# <b>Fork Count :</b> <i>{qw.get("forks_count")}</i>

# <b>Open Issues :</b> <i>{qw.get("open_issues")}</i>
# """
        txt = f"""
<b>𝐅𝐮𝐥𝐥 𝐍𝐚𝐦𝐞 : </b> <i>{qw.get("full_name")}</i>

<b>𝐋𝐢𝐧𝐤 :</b> {qw.get("html_url")}

<b>𝐅𝐨𝐫𝐤 𝐂𝐨𝐮𝐧𝐭 : </b> <i>{qw.get("forks_count")}</i>

<b>𝐎𝐩𝐞𝐧 𝐈𝐬𝐬𝐮𝐞𝐬 : </b> <i>{qw.get("open_issues")}</i>

𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬 : <a href='https://github.com/search?q={args}+language%3APython&type=repositories&l=Python&s=updated&o=desc'>{args}</a>
"""        
        if qw.get("description"):
            txt += f'<b>Description :</b> <code>{qw.get("description")}</code> \n'

        if qw.get("language"):
            txt += f'<b>Language :</b> <code>{qw.get("language")}</code> \n'

        if qw.get("size"):
            txt += f'<b>Size :</b> <code>{qw.get("size")}</code> \n'

        if qw.get("score"):
            txt += f'<b>Score :</b> <code>{qw.get("score")}</code> \n'

        if qw.get("created_at"):
            txt += f'<b>Created At :</b> <code>{qw.get("created_at")}</code> \n'

        if qw.get("archived") == True:
            txt += f"<b>This Project is Archived</b> \n"
#        await pablo.edit(txt, disable_web_page_preview=True)
    
#    search = https://github.com/search?q={args}+language%3APython&type=repositories&l=Python&s=updated&o=desc

#        await pablo.edit(f"https://github.com/search?q={args}+language%3APython&type=repositories&l=Python&s=updated&o=desc", disable_web_page_preview=True)
        await pablo.edit(txt, disable_web_page_preview=True)


