
# ADD THIS ALL REQUERMENT.PY #

# pyTelegramBotAPI==4.14.0
# beautifulsoup4~=4.8.2
# certifi==2019.6.16
# chardet==3.0.4
# idna==2.8
# six==1.12.0
# urllib3==1.25.3
 



import telebot
import requests

# Ganti 'TOKEN_BOT_ANDA' dengan token bot Telegram Anda
BOT_TOKEN = '2108094040:AAHY_MkFF5X5HhW4yaZzq49jduK2fySPlhM'
bot = telebot.TeleBot(BOT_TOKEN)

# Ganti 'TOKEN_REMOVEBG_API' dengan token API Remove.bg Anda
REMOVEBG_API_KEY = 'MJMoiiatXPHcHgFG3D1Wf2aG'

# @BOT.message_handler(commands=["check", ], chat_types=["private", ], func=_is_master)

# if message.reply_to_message.content_type == "photo":



# @bot.message_handler(content_types=['photo'])
@bot.message_handler(commands=["reverse"])
def handle_photo(message):
    try:
        file_id = message.reply_to_message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"

        # Kirim permintaan ke Remove.bg API untuk menghapus background gambar
        response = requests.post('https://api.remove.bg/v1.0/removebg', data={'image_url': file_url}, headers={'X-Api-Key': REMOVEBG_API_KEY})

        if response.status_code == 200:
            # Simpan gambar hasil dan kirimkan ke pengguna
            with open('removed_bg.png', 'wb') as f:
                f.write(response.content)
            bot.send_document(message.chat.id, open('removed_bg.png', 'rb'))
        else:
            bot.reply_to(message, "Maaf, tidak dapat menghapus background gambar.")

    except Exception as e:
        bot.reply_to(message, "An error occurred while processing the image..")





# @bot.message_handler(content_types=['photo'])
# def handle_photo(message):
#     try:
#         file_id = message.photo[-1].file_id
#         file_info = bot.get_file(file_id)
#         file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"
# 
#         # Kirim permintaan ke Remove.bg API untuk menghapus background gambar
#         response = requests.post('https://api.remove.bg/v1.0/removebg', data={'image_url': file_url}, headers={'X-Api-Key': REMOVEBG_API_KEY})
# 
#         if response.status_code == 200:
#             # Simpan gambar hasil dan kirimkan ke pengguna
#             with open('removed_bg.png', 'wb') as f:
#                f.write(response.content)
#             bot.send_document(message.chat.id, open('removed_bg.png', 'rb'))
#         else:
#             bot.reply_to(message, "Maaf, tidak dapat menghapus background gambar.")
# 
#     except Exception as e:
#         bot.reply_to(message, "An error occurred while processing the image..")




# bot.polling()
