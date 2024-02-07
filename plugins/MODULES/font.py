# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import os
from plugins.helpers.fotnt_string import Fonts
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.private & filters.command(["font"]))
async def style_buttons(c, m, cb=False):
    buttons = [[
        InlineKeyboardButton('𝙽𝙰𝙼𝙴-10', callback_data='style+one'),
        InlineKeyboardButton('ℕ𝔸𝕄𝔼-𝟙𝟘', callback_data='style+two')
        ],[        
        InlineKeyboardButton('𝐍𝐀𝐌𝐄-𝟏𝟎', callback_data='style+three'),
        InlineKeyboardButton('𝑵𝑨𝑴𝑬-10', callback_data='style+four')
        ],[        
        InlineKeyboardButton('𝗡𝗔𝗠𝗘-𝟭𝟬', callback_data='style+five'),
        InlineKeyboardButton('Ⓝ︎Ⓐ︎Ⓜ︎Ⓔ︎-①⓪', callback_data='style+six')
        ],[
        InlineKeyboardButton('🅝︎🅐︎🅜︎🅔︎-➊⓿', callback_data='style+seven'),
        InlineKeyboardButton('𝐂𝐋𝐎𝐒𝐄 𝐃𝐀𝐓𝐀', callback_data='close_data')
    ]]
    if not cb:
        if ' ' in m.text:
            title = m.text.split(" ", 1)[1]
            await m.reply_text(title, reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=m.id)                     
        else:
            await m.reply_text(text="Ente Any Text Eg:- `/font [text]`")    
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
        


@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'one':
        cls = Fonts.one
    if style == 'two':
        cls = Fonts.two
    if style == 'three':
        cls = Fonts.three
    if style == 'four':
        cls = Fonts.four
    if style == 'five':
        cls = Fonts.five
    if style == 'six':
        cls = Fonts.six
    if style == 'seven':
        cls = Fonts.seven
    

    r, oldtxt = m.message.reply_to_message.text.split(None, 1) 
    new_text = cls(oldtxt)            
    try:
        await m.message.edit_text(f"`{new_text}`\n\n👆 Click To Copy", reply_markup=m.message.reply_markup)
    except Exception as e:
        print(e)



