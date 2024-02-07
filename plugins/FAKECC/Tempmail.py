import os
import asyncio
import requests
import random
import bs4

from pykeyboard import InlineKeyboard
from pyrogram.errors import UserNotParticipant
from pyrogram import filters, Client
from RandomWordGenerator import RandomWord
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message  #  CallbackQuery
from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid, bad_request_400


 

#********************************************************************************




    
#********************************************************************************
API1='https://www.1secmail.com/api/v1/?action=getDomainList'
API2='https://www.1secmail.com/api/v1/?action=getMessages&login='
API3='https://www.1secmail.com/api/v1/?action=readMessage&login='
#********************************************************************************
from pyrogram import *
import requests as re
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import wget
import os 


create = InlineKeyboardMarkup(
            [[InlineKeyboardButton("SMΛЯT TΞϾH 🇱🇰", url="https://t.me/nasrani_update")]])


buttons=InlineKeyboardMarkup(
                             [
                             [
            InlineKeyboardButton('Generate', callback_data='rename'),
            InlineKeyboardButton('Refresh', callback_data='refresh'),
            InlineKeyboardButton('Close', callback_data='close')
                   ] 
                             ])

msg_buttons=InlineKeyboardMarkup(
                             [
                             [
            InlineKeyboardButton('View message', callback_data='view_msg'),
            InlineKeyboardButton('Close', callback_data='close')
                   ] 
                             ])



email=''
@Client.on_message(filters.command('tempmail'))
async def start_msg(client,message):
    await message.reply("**Hey "+message.from_user.first_name+" !!**\n @NASRANI_SUPPORT is a free service that allows to generates and receive emails at a temporary address that self-destructed after a certain time elapses.\n\n**__ How It Safe's You??**__\n- Using the temporary mail allows you to completely protect your real mailbox against the loss of personal information. Your temporary e-mail address is completely anonymous. Your details: information about your person and users with whom you communicate, IP-address, e-mail address are protected and completely confidential.")
    await message.reply("**Generate a Email Now❕**",
                        reply_markup=buttons)


@Client.on_callback_query(filters.regex('rename'))
async def mailboxx(client,message):
#    response=message.data
#    if response=='generate':
    global email
    email = re.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()[0]
    await message.edit_message_text('__**Your Temporary E-mail: **__`'+str(email)+'`',
                                       reply_markup=buttons)
    print(email)


@Client.on_callback_query(filters.regex('refresh'))
async def refresh(client,message):
    print(email)
    try:
        if email=='':
            await message.edit_message_text('Genaerate a email',reply_markup=buttons)
        else: 
            getmsg_endp =  "https://www.1secmail.com/api/v1/?action=getMessages&login=" + email[:email.find("@")] + "&domain=" + email[email.find("@") + 1:]
            print(getmsg_endp)
            ref_response = re.get(getmsg_endp).json()
            global idnum
            idnum=str(ref_response[0]['id'])
            from_msg=ref_response[0]['from']
            subject=ref_response[0]['subject']
            refreshrply='You a message from '+from_msg+'\n\nSubject : '+subject
            await message.edit_message_text(refreshrply,
                                            reply_markup=msg_buttons)
    except:
            
        await message.answer('No messages were received..\nin your Mailbox '+email)

@Client.on_callback_query(filters.regex('view_msg'))
async def view_msg(client,message):
        msg =re.get("https://www.1secmail.com/api/v1/?action=readMessage&login=" + email[:email.find("@")] + "&domain=" + email[email.find("@") + 1:] + "&id=" + idnum).json()
        print(msg)
        from_mail=msg['from']
        date=msg['date']
        subjectt=msg['subject']
        try:
          attachments=msg['attachments'][0]
        except:
            pass
        body=msg['body']
        mailbox_view='ID No : '+idnum+'\nFrom : '+from_mail+'\nDate : '+date+'\nSubject : '+subjectt+'\nmessage : \n'+body
        await message.edit_message_text(mailbox_view,reply_markup=buttons)
        mailbox_view='ID No : '+idnum+'\nFrom : '+from_mail+'\nDate : '+date+'\nSubject : '+subjectt+'\nmessage : \n'+body
        if attachments == "[]":
            await message.edit_message_text(mailbox_view,reply_markup=buttons)
            await message.answer(f"No Messages Were Recieved..", show_alert=True)
        else:
            dlattach=attachments['filename']
            attc="https://www.1secmail.com/api/v1/?action=download&login=" + email[:email.find("@")] + "&domain=" + email[email.find("@") + 1:] + "&id=" + idnum+"&file="+dlattach
            print(attc)
            mailbox_vieww='ID No : '+idnum+'\nFrom : '+from_mail+'\nDate : '+date+'\nSubject : '+subjectt+'\nmessage : \n'+body+'\n\n'+'[Download]('+attc+') Attachments'
            filedl=wget.download(attc)
            await message.edit_message_text(mailbox_vieww,reply_markup=buttons)
            os.remove(dlattach)
    
#********************************************************************************

@Client.on_message(filters.command("domains"))
async def fakemailgen(client, message):
    name = message.from_user.id
    x = requests.get(f'https://www.1secmail.com/api/v1/?action=getDomainList').json()
    xx = str(",".join(x))
    email = xx.replace(",", "\n")
    await client.send_message(
    name, 
    text = f"""
**{email}**
""",
    reply_markup = create)
