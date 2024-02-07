from pyrogram import Client, filters, idle
import pyrogram, asyncio, random, time
from pyrogram.errors import FloodWait
from pyrogram.types import *
import requests
from pyrogram import Client, types, filters, enums


import re
import urllib
import urllib.request

import bs4
import requests
from bs4 import BeautifulSoup
from pyrogram import filters






@Client.on_message(filters.command("logo"))
async def logo(bot, msg):
    if len(msg.command) == 1:
       return await msg.reply_text("Usage:\n\n /logo Jeol")
    logo_name = msg.text.split(" ", 1)[1]
    API = f"https://api.sdbots.tech/logohq?text={logo_name}"
    req = requests.get(API).url
    await msg.reply_photo(
        photo=f"{req}")

@Client.on_message(filters.command("animelogo"))
async def logo(bot, msg):
    if len(msg.command) == 1:
       return await msg.reply_text("Usage:\n\n /animelogo Jeol")
    logo_name = msg.text.split(" ", 1)[1]
    API = f"https://api.sdbots.tech/anime-logo?name={logo_name}"
    req = requests.get(API).url
    await msg.reply_photo(
        photo=f"{req}")




@Client.on_message(filters.command("anime"))
async def anime(client, message):
    user_name = message.from_user.username
    if len(message.command) < 2:
        return await message.reply_text(f"{user_name} Send **/anime AnimeName** to get info ℹ️.")
    message.command.pop(0)
    name = " ".join(message.command)
    res = requests.get(f"https://kitsu.io/api/edge//anime?filter[text]={name}")

    search_result = res.json()["data"]

    if len(search_result) < 1:
        return await message.reply_text("404 Anime not found")

    await message.reply_photo(
        photo=search_result[0]["attributes"]["posterImage"]["original"],
    )
    await message.reply(
        f"{user_name} \n **Title**:{search_result[0]['attributes']['titles']['en']}\n**Japanese**:{search_result[0]['attributes']['titles']['en_jp']}\n**PopularityRank**:{search_result[0]['attributes']['popularityRank']}\n**Age Rating**:{search_result[0]['attributes']['ageRatingGuide']}\n**Episode Count**:{search_result[0]['attributes']['episodeCount']}\n**Synopsis**:{search_result[0]['attributes']['synopsis']}",
    )










@Client.on_message(filters.command("app"))
async def apk(client, message):
    try:
        lgcd = message.text.split("/app", 1)[1]
			
        lg_cd = lgcd[1].lower().replace(" ", "")
        final_name = "+".join(lg_cd)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += (
            "\n\n<code>Developer :</code> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n<code>Rating :</code> " + app_rating.replace(
            "Rated ", "⭐ "
        ).replace(" out of ", "/").replace(" stars", "", 1).replace(
            " stars", "⭐ "
        ).replace(
            "five", "5"
        )
        app_details += (
            "\n<code>Features :</code> <a href='"
            + app_link
            + "'>View in Play Store</a>"
        )
        app_details += "\n\n===> @DaisySupport_Official <==="
        await message.reply(page)
    except IndexError:
        await message.reply("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await message.reply("Exception Occured:- " + str(err))
