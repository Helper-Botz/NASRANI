import os
from utils import temp

from asyncio import sleep
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
import random
from info import SP




Muhammed = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)





ADS = f"""
𝐇𝐞𝐥𝐥𝐨\n
𝙉𝙚𝙬 𝙁𝙞𝙡𝙢 𝙇𝙤𝙬 𝙎𝙞𝙯𝙚 𝙈𝙤𝙫𝙞𝙚𝙨 𝘼𝙙𝙙𝙚𝙙 𝙏𝙝𝙞𝙨 𝘾𝙝𝙖𝙣𝙣𝙚𝙡...\n
𝐅𝐚𝐬𝐭𝐞𝐬𝐭 𝐀𝐝𝐝𝐞𝐝 𝐓𝐡𝐢𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥...\n
𝐅𝐚𝐬𝐭 𝐉𝐨𝐢𝐧 𝐓𝐡𝐢𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥...\n
"""





MESSAGE = """
𝐓𝐧𝐱 𝐀𝐥𝐥 𝐔𝐬𝐞𝐫𝐬🥰🥰\n

𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐀𝐧𝐧𝐝 𝐒𝐡𝐚𝐫𝐞\n

<i>നിങ്ങളുടെ ഗ്രൂപ്പിൽ എന്നെ ആഡ് ചെയ്ത് അഡ്മിൻ ആക്കിക്കോ. എല്ലാ മൂവിയും കിട്ടും..\n
ഗ്രൂപ്പ് ഇല്ലെങ്കിൽ ഒരു ഗ്രൂപ്പ്‌ ഉണ്ടാക്കി</i>
<a href='http://t.me/{}?startgroup=true'>@𝐌𝐢𝐧𝐧𝐚𝐥_𝐌𝐮𝐫𝐚𝐥𝐢_𝐑𝐨𝐛𝐨𝐭</a><i> നെ അല്ലെങ്കിൽ</i>

<a href='http://t.me/nasrani_bot?startgroup=true'>@𝐍𝐀𝐒𝐑𝐀𝐍𝐈_𝐁𝐎𝐓</a><i>നെ ആഡ് ചെയ്തു അഡ്മിൻ ആക്കിക്കോ..

എന്നിട്ട് ചോദിക്കുന്ന മൂവീസ് അപ്പപ്പോൾ തന്നെ നിങ്ങളുടെ വിരൽ തുമ്പിൽ കിട്ടുന്നതാണ്..😌😌</i>\n\n

𝐈𝐭𝐬 𝐄𝐚𝐬𝐲 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞; 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐬 𝐀𝐝𝐦𝐢𝐧, 𝐓𝐡𝐚𝐭𝐬 𝐀𝐥𝐥, 𝐢 𝐰𝐢𝐥𝐥 𝐏𝐫𝐨𝐯𝐢𝐝𝐞 𝐌𝐨𝐯𝐢𝐞𝐬 𝐓𝐡𝐞𝐫𝐞...🤓\n\n

𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐁𝐢𝐠𝐠𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 𝐟𝐢𝐥𝐭𝐞𝐫 𝐛𝐨𝐭 @𝐦𝐢𝐧𝐧𝐚𝐥_𝐦𝐮𝐫𝐚𝐥𝐢_𝐫𝐨𝐛𝐨𝐭 𝐨𝐫 @𝐍𝐀𝐒𝐑𝐀𝐍𝐈_𝐁𝐎𝐓

𝐀𝐥𝐥 𝐟𝐢𝐥𝐦𝐬 𝐚𝐝𝐝𝐞𝐝 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭. 😌😌

𝐅𝐚𝐬𝐭 𝐣𝐨𝐢𝐧....
"""



@Client.on_message(filters.private & filters.command(["sub"]))
async def sub(client, message):
    search = message.text           
    buttons = [[
        InlineKeyboardButton('𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
    ],[
        InlineKeyboardButton('𝐌𝐨𝐯𝐢𝐞𝐬 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/NasraniSeries'),
        InlineKeyboardButton('𝐒𝐨𝐧𝐠 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/NasraniChatGroup')
    ],[
        InlineKeyboardButton('𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/testpubliconly'),
        InlineKeyboardButton('𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/bigmoviesworld')
    ],[
        InlineKeyboardButton('𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url=f'https://t.me/+obGgfOP2LZ0wYTBl')
    ]] 
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(
    chat_id=message.chat.id,
    photo=random.choice(SP),
    caption=MESSAGE.format(temp.U_NAME, message.text),
    reply_markup=reply_markup, 
    parse_mode=enums.ParseMode.HTML
)






@Client.on_message(filters.private & filters.command(["ads"]))
async def ads(client, message):
    search = message.text         
    buttons = [[
        InlineKeyboardButton('𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋', url=f'https://t.me/bigmoviesworld')   
    
    ],[
        InlineKeyboardButton("𝐃𝐞𝐥𝐞𝐭𝐞", callback_data = "delete"),
        InlineKeyboardButton("𝐈𝐦𝐩𝐨𝐫𝐭𝐚𝐧𝐭", callback_data = "answ")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(
    chat_id=message.chat.id,
    photo=random.choice(SP),
    caption=ADS.format(message.text),
    reply_markup=reply_markup, 
    parse_mode=enums.ParseMode.HTML
    )



