import os
import time
import ytthumb
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["ytthumb", 'dlthumb']))
async def send_thumbnail(bot, update):
    message = await update.reply_text(
        text="`Analysing...🤒`",
        disable_web_page_preview=True,
        quote=True
    )
    try:
        if " | " in update.text:
            video = update.text.split(" | ", -1)[0]
            quality = update.text.split(" | ", -1)[1]
        else:
            video = update.text
            quality = "hd"
        thumbnail = ytthumb.thumbnail(
            video=video,
            quality=quality
        )
        await update.reply_photo(
            photo=thumbnail,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⭕Source⭕', url='https://t.me/nasrani_update')]]),
            quote=True
        )
        await message.delete()
    except Exception as error:
        await message.edit_text(
            text="**Please Use** /ytthumb (youtube link)\n\n**Example:** `/ytthumb https://youtu.be/TPHPMAS0TMc?si=E76ktK8En6WweiPU`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('JOIN UPDATE CHANNEL', url='https://t.me/kinzanoufal')]]))
