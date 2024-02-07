import datetime
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import pytz
import os
from datetime import datetime
from pytz import timezone
from pyrogram import Client, filters
from datetime import datetime
import pytz


from datetime import datetime
import pytz

time_str = """
**TIME** :- `{}`

**DATE** :- `{}`

**DAY** :- `{}`

**UTC** :- `{}`

**UNIX TIME** :- `{}`

**TIME ZONE** :- `{}`
"""


class TimeTeller:
    def india():
        present = datetime.now(tz=pytz.timezone("Asia/Kolkata"))
        time = present.strftime("%I:%M:%S %p")
        date = present.strftime("%d-%B-%Y")
        day = present.strftime("%A")
        utc = present.strftime("%z")
        unixtime = int(datetime.utcnow().timestamp())
        indian_time = time_str.format(time, date, day, utc, unixtime, "Asia/Kolkata")
        return indian_time

    def gmt():
        present = datetime.now(tz=pytz.timezone('GMT'))
        time = present.strftime("%I:%M:%S %p")
        date = present.strftime("%d-%B-%Y")
        day = present.strftime("%A")
        utc = present.strftime("%z")
        unixtime = int(datetime.utcnow().timestamp())
        gmt_time = time_str.format(time, date, day, utc, unixtime, "GMT")
        return gmt_time

    def particular(time_zone):
        try:
            present = datetime.now(tz=pytz.timezone(time_zone))
            time = present.strftime("%I:%M:%S, %p")
            date = present.strftime("%d-%B-%Y")
            day = present.strftime("%A")
            utc = present.strftime("%z")
            unixtime = int(datetime.utcnow().timestamp())
            particular_time = time_str.format(time, date, day, utc, unixtime, time_zone)
        except pytz.exceptions.UnknownTimeZoneError:
            particular_time = f"**Unknown Time Zone ** : '`{time_zone}`' is not a valid timezone. \n\n" \
                              "1) Send /timezones to check all timezones. \n" \
                              "2) Use '/search country/city' to search for  particular timezone."
        return particular_time


@Client.on_message(filters.command("time"))
async def default_time(timebot, msg):
    if len(msg.command) == 1:
        time = TimeTeller.india()
        await msg.reply(time, quote=True)
    elif len(msg.command) == 2:
        time_zone = msg.command[1]
        time = TimeTeller.particular(time_zone)
        await msg.reply(time, quote=True)
    else:
        await msg.reply(
            "**Incorrect Time Zone** \n\nTime Zones are of only one word with format 'country/city' \n\nPlease Check all timezones by sending /timezones",
            quote=True)




def get_current_time():
    tz = pytz.timezone('Asia/Kolkata')  # Setting the timezone to India (Kolkata)
    current_time = datetime.now(tz)
    return current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

@Client.on_message(filters.command(["Times"]))
def send_time(client, message):
    time = get_current_time()
    client.send_message(message.chat.id, f"Current time in India: {time}")
