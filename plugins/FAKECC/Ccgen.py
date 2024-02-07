from SafoneAPI import SafoneAPI

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
api = SafoneAPI()

@Client.on_message(filters.command(["fakegen", "fakecc"], [".", "!", "/"]))
async def gen_cc(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Please Give Me a Bin To\nGenerate Cc ...")

    try:
        await message.delete()
    except:
        pass

    aux = await message.reply_text("Generating ...")
    bin = message.text.split(None, 1)[1]

    if len(bin) < 6:
        return await aux.edit("❌ Wrong Bin❗...")

    try:
        resp = await api.ccgen(bin, 10)
        cards = resp.liveCC

        regenerate_button = InlineKeyboardButton(
            "√ʀᴇɢᴇɴᴇʀᴀᴛᴇ¹", callback_data=f"regenerate_{bin}"
        )
        keyboard = InlineKeyboardMarkup([[regenerate_button]])

        await aux.edit(
            f"""
➤ Sᴏᴍᴇ Lɪᴠᴇ Gᴇɴᴇʀᴀᴛᴇᴅ Cᴄ ➻

╭✠╼━━━━━━❖━━━━━━━✠╮ 

{cards[0]}\n{cards[1]}\n{cards[2]}
{cards[3]}\n{cards[4]}\n{cards[5]}
{cards[6]}\n{cards[7]}\n{cards[8]}
{cards[9]}\n
╰✠╼━━━━━━❖━━━━━━━✠╯

⦿ Bɪɴ: `{resp.results[0].bin}`
⦿ Tɪᴍᴇ Tᴏᴏᴋ: {resp.took}\n\n @NASRANI_SUPPORT""",
            reply_markup=keyboard,
        )

    except Exception as e:
        return await aux.edit(f"Error: {e}.")

# @Client.on_callback_query(filters.regex(r"regenerate_"))
# async def regenerate_cc(client, callback_query):
#    bin_to_regenerate = callback_query.data.split("_")[1]

#    try:
#        resp = await api.ccgen(bin_to_regenerate, 10)
        cards = resp.liveCC
#
#         await callback_query.edit_message_text(
#             f"""
# ➤ Sᴏᴍᴇ Lɪᴠᴇ Gᴇɴᴇʀᴀᴛᴇᴅ Cᴄ ➻

# ╭✠╼━━━━━━❖━━━━━━━✠╮ 

# {cards[0]}\n{cards[1]}\n{cards[2]}
# {cards[3]}\n{cards[4]}\n{cards[5]}
# {cards[6]}\n{cards[7]}\n{cards[8]}
# {cards[9]}\n
# ╰✠╼━━━━━━❖━━━━━━━✠╯

# ⦿ Bɪɴ: `{resp.results[0].bin}`
# ⦿ Tɪᴍᴇ Tᴏᴏᴋ: {resp.took}\n\n @NASRANI_SUPPORT""",
#        )

#    except Exception as e:
#        await callback_query.edit_message_text(f"Error: {e}.")
