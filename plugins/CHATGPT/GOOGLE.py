# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import requests
from bs4 import BeautifulSoup
from googlesearch import search
from pyrogram import Client, filters
from pyrogram.types import Message




async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)


eor = edit_or_reply



def googlesearch(query):
    co = 1
    returnquery = {}
    for j in search(query):
        url = str(j)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        metas = soup.find_all("meta")
        site_title = None
        for title in soup.find_all("title"):
            site_title = title.get_text()
        metadeta = [
            meta.attrs["content"]
            for meta in metas
            if "name" in meta.attrs and meta.attrs["name"] == "description"
        ]
        returnquery[co] = {"title": site_title, "metadata": metadeta, "url": j}
        co = co + 1
    return returnquery


@Client.on_message(filters.command(["gs", "google"]))
async def gs(client, message):
    Man = await edit_or_reply(message, "`Processing...`")
    msg_txt = message.text
    returnmsg = ""
    query = None
    if " " in msg_txt:
        query = msg_txt[msg_txt.index(" ") + 1 : len(msg_txt)]
    else:
        await Man.edit("Give a query to search")
        return
    results = googlesearch(query)
    for i in range(1, 10, 1):
        presentquery = results[i]
        presenttitle = presentquery["title"]
        presentmeta = presentquery["metadata"]
        presenturl = presentquery["url"]
        print(presentquery)
        print(presenttitle)
        print(presentmeta)
        print(presenturl)
        if not presentmeta:
            presentmeta = ""
        else:
            presentmeta = presentmeta[0]
        returnmsg = (
            returnmsg
            + f"[{str(presenttitle)}]({str(presenturl)})\n{str(presentmeta)}\n\n"
        )
    await Man.edit(returnmsg)
    
