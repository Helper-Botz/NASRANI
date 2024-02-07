import os
from pyrogram import Client, filters, enums


DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

bughunter0 = Client(
    "Mp4-to-Mp3-Conveter",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")



@Client.on_message(filters.audio & filters.private)
async def mp3(bot, message):

    # download video
    file_path = DOWNLOAD_LOCATION + f"{message.from_user.id}.mp3"
    txt = await message.reply_text("Downloading to My server.....")
    await message.download(file_path)
    await txt.edit_text("Downloaded Successfully")
    
    # convert to audio
    await txt.edit_text("Converting to audio")
    await bot.send_audio(audio=file_path, chat_id=message.chat.id, caption="@nasrani_update")
    
    # remove file
    try:
        os.remove(file_path)
    except:
        pass
    
    await txt.delete()
