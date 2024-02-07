from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters

"""Edit ചെയ്യുന്നവനോട്.. നിന്റെ തന്ത അല്ല ഈ code ഉണ്ടാക്കിയത് """

@Client.on_message(filters.photo & filters.command(["rmbg"]))
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Select your required mode from below!ㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="𝖱𝖾𝗆𝗈𝗏𝖾 𝖡𝖦", callback_data="removebg")                        
                    ]
                ]
            ),
            reply_to_message_id=message.id,
        )                    
                    
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return
