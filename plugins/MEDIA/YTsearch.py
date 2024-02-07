import logging
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from pyrogram import filters, Client
# from config import BOT_USERNAME
import asyncio
from info import SUPPORT_CHAT_ID



@Client.on_message(filters.command("yt_search") & filters.chat(SUPPORT_CHAT_ID))
async def ytsearchh(bot, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/search needs an argument!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text(" searching")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"Judul: {results[i]['title']}\n"
            text += f"Durasi: {results[i]['duration']}\n"
            text += f"Views: {results[i]['views']}\n"
            text += f"Channel: {results[i]['channel']}\n"
            text += f"https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        k = await m.edit(text, disable_web_page_preview=True)
        await asyncio.sleep(120)
        await k.delete()
        await message.delete()
    except Exception as e:
        await m.edit(str(e))
