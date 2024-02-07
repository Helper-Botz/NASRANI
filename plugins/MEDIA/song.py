from __future__ import unicode_literals
from utils import temp
import os
import requests
import aiohttp
import yt_dlp
import asyncio
import math
import time
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import FILE_CHANNEL, FILE_FORWARD, SP
import wget
import aiofiles
from Script import script
from pyrogram import filters, Client, enums
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
import youtube_dl
import requests

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))



@Client.on_message(filters.chat(-1001203428484) & filters.text & filters.command('song'))
async def song(client, message):
    if len(message.command) == 1:
       return await message.reply_text("Give an input!")
    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    chat_id = message.chat.id
    args = message.text.split(None, 1)[1]
    r = requests.get(f"https://saavn.me/search/songs?query={args}&page=1&limit=1").json()
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
  #  album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp4", "mp3")
    os.rename(file, ffile)
    m=await message.reply_text(f"𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐅𝐨𝐫 𝐒𝐚𝐚𝐯𝐧..")
    buttons = [[
        InlineKeyboardButton("JOIN MOVIES", url="https://t.me/NASRANI_UPDATE")
    ]]
    k = await client.send_audio(audio=ffile,chat_id=chat_id, caption=f"𝐇𝐞𝐥𝐥𝐨 {message.from_user.mention} \n`{sname}` \n 𝐅𝐫𝐨𝐦 : @nasrani_update ",thumb=thumbnail,
    reply_markup=InlineKeyboardMarkup(buttons)
    )
#    Joel_tgx = await message.reply_text(
#                        
#        text=script.SONG_CAP.format(message.from_user.mention, sname),
#        parse_mode=enums.ParseMode.HTML,
#        reply_markup=InlineKeyboardMarkup(
#            [
#             [
#              InlineKeyboardButton('📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐧𝐤 📥 ', url = k.link)
#          ],[
#              InlineKeyboardButton("⚠️ 𝐂𝐚𝐧'𝐭 𝐀𝐜𝐜𝐞𝐬𝐬 ❓ 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 ⚠️", url=(FILE_FORWARD))
#             ]
#            ]
#        )
#    )
#    await asyncio.sleep(60)
#    await Joel_tgx.delete()
    await m.delete()

  
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = await message.reply("𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐅𝐨𝐫 𝐘𝐨𝐮𝐭𝐮𝐛𝐞..")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        performer = f"[Autofilter - Master]" 
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "**𝙵𝙾𝚄𝙽𝙳 𝙽𝙾𝚃𝙷𝙸𝙽𝙶 𝙿𝙻𝙴𝙰𝚂𝙴 𝙲𝙾𝚁𝚁𝙴𝙲𝚃 𝚃𝙷𝙴 𝚂𝙿𝙴𝙻𝙻𝙸𝙽𝙶 𝙾𝚁 𝚂𝙴𝙰𝚁𝙲𝙷 𝙰𝙽𝚈 𝙾𝚃𝙷𝙴𝚁 𝚂𝙾𝙽𝙶**"
        )
        print(str(e))
        return
    m.edit("🥺𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐅𝐨𝐫 𝐘𝐨𝐮𝐭𝐮𝐛𝐞..")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
#        rep = f"𝐇𝐞𝐥𝐥𝐨 {message.from_user.mention} \n\n <a href="https://t.me/nasrani_update">🎧𝐍𝐚𝐬𝐫𝐚𝐧𝐢_𝐔𝐩𝐝𝐚𝐭𝐞🎧</a>"
        rep = script.Y_TXT.format(message.from_user.mention, title)
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        buttons = [[
            InlineKeyboardButton("JOIN MOVIES", url="https://t.me/NASRANI_UPDATE")
        ]]
        k = await message.reply_audio(audio=audio_file, caption=rep, parse_mode=enums.ParseMode.HTML,quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name,
#        k = await message.reply_audio(audio=audio_file, caption=f"𝐇𝐞𝐥𝐥𝐨 {message.from_user.mention}", parse_mode=enums.ParseMode.MARKDOWN,quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name,
                                    
        reply_markup=InlineKeyboardMarkup(buttons)
        )
        
#        buttons = [[
#        InlineKeyboardButton("JOIN MOVIES", url="https://t.me/NASRANI_UPDATE")
#        ]]                           
        
#        reply_markup=InlineKeyboardMarkup(buttons)
#        )
#        await asyncio.sleep(60)
#        await k.delete()
#        await Joel_tgx.delete()
        await m.delete()
       
    except Exception as e:
        m.edit("**🚫 𝙴𝚁𝚁𝙾𝚁 🚫**")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

def get_text(message: Message) -> [None,str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None


@Client.on_message(filters.chat(-1001203428484) & filters.text & filters.command('video'))
async def vsong(client, message: Message):
    if len(message.command) == 1:
       return await message.reply_text("Give an input!")

    args = message.text.split(None, 1)[1]
    r = requests.get(f"https://saavn.me/search/songs?query={args}&page=1&limit=1").json()
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
  #  album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp3", "mp4")
    os.rename(file, ffile)
    m=await message.reply_text(f"𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐅𝐨𝐫 𝐒𝐚𝐚𝐯𝐧..")
    buttons = [[
        InlineKeyboardButton("JOIN MOVIES", url="https://t.me/NASRANI_UPDATE")
    ]]
    k = await message.reply_video(video=ffile, caption=f"[{sname}]({r['data']['results'][0]['url']}) - from @nasrani_update ",thumb=thumbnail,
    reply_markup=InlineKeyboardMarkup(buttons)
    )
    await m.delete()
    urlissed = get_text(message)

    pablo = await client.send_message(
        message.chat.id, f"𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐅𝐨𝐫 𝐘𝐨𝐮𝐭𝐮𝐛𝐞.. `{urlissed}`"
    )
    if not urlissed:
        await pablo.edit("Invalid Command Syntax Please Check help Menu To Know More!")
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await event.edit(event, f"**𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙵𝚊𝚒𝚕𝚎𝚍 𝙿𝚕𝚎𝚊𝚜𝚎 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗..♥️** \n**Error :** `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"""
𝐓𝐢𝐭𝐥𝐞 : [{thum}]({mo})
𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐁𝐲 : `{message.from_user.mention}`
@𝐍𝐚𝐬𝐫𝐚𝐧𝐢_𝐔𝐩𝐝𝐚𝐭𝐞
"""
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,        
        reply_to_message_id=message.id 
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
