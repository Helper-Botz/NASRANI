from pyrogram import Client, filters
import random
VALID_PREFIXES = [4, 5, 6,3]  # VISA starts with 4, MasterCard with 5, Discover with 6

def generate_test_card_number(prefix, length):
    card_number = [random.randint(0, 9) for _ in range(length - len(str(prefix)) - 1)]
    card_number.insert(0, str(prefix))
    card_number = ''.join(map(str, card_number))
    checksum = luhn_checksum(int(card_number) * 10)
    return card_number + str((10 - checksum) % 10)



@Client.on_message(filters.command("genbin"))
def generate(client,message):
    prefix = random.choice(VALID_PREFIXES)
    length = 6  # Standard credit card length
    card_number = generate_test_card_number(prefix, length)
    message.reply_text(f"𝗕𝗜𝗡 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘𝗗\n" f"{card_number} ✅")
