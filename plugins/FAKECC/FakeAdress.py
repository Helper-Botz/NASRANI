from pyrogram import Client, filters
import random
from faker import Faker

# Create a Faker instance
fake = Faker()

# Constants
VALID_PREFIXES = [4, 5, 6,3]  # VISA starts with 4, MasterCard with 5, Discover with 6



# Generate person info command handler
@Client.on_message(filters.command("rand"))
def generate_info(client, message):
    # Generate fake data
    name = fake.name()
    address = fake.address()
    country = fake.country()
    phone_number = fake.phone_number()
    email = fake.email()
    city = fake.city()
    state = fake.state()
    zipcode = fake.zipcode()

    # Create a message with the fake data
    info_message = (
        f"**Full Name:** {name}\n"
        
        f"**Address:** {address}\n"
        
        f"**Country:** {country}\n"
        
        f"**Phone Number:** {phone_number}\n"
        
        f"**Email:** {email}\n"
        
        f"**City:** {city}\n"
        
        f"**State:** {state}\n"
        
        f"**zipcode:** {zipcode}"
        
    )

    # Send the fake data to the user
    message.reply_text(info_message)

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10
