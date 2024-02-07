from pyrogram import Client, filters 
from pyrogram.types import Message
from info import ADMINS
import asyncio
from pyrogram import filters, Client, enums
from pyrogram.types import Message 
import random



from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import math
import os
import shlex
from typing import Tuple
from pyrogram.types import Message

spam_chats = []

RUN_STRINGS = (
    "5",
    "10",
    "25",
    "50",    
    "100",
    "120",
    "150",
    "180",        
)




def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])



def content(msg) -> [None, str]:
    text_to_return = msg.text



@Client.on_message(filters.command("all"))
async def all(client, message):
    await message.delete()
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    sh = content(message)
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not sh:
        return await message.edit("**Berikan saya pesan atau balas ke pesan!**")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 5:
            if sh:
                txt = f"{query}\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(f"{query} \n{usrtxt}")
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass




@Client.on_message(filters.command("tagall"))
async def mentionall(client, message):
    await message.delete()
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.edit("**Berikan saya pesan atau balas ke pesan!**")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 500:
            if args:
                txt = f"{args}\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@Client.on_message(filters.command("cancel"))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.edit("**Sepertinya tidak ada tagall disini.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**Memberhentikan Mention.**")






