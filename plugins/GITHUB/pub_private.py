from pyrogram import Client, filters
import requests
from plugins.helpers.config import ADMINS, GIT_TOKEN

# import plugins.helpers.config


# Replace 'YOUR_GITHUB_TOKEN' with your GitHub token
github_token = GIT_TOKEN






GIT_TOKEN = GIT_TOKEN



def create_github_repo(repo_name):
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {GIT_TOKEN}"}
    data = {"name": repo_name, "auto_init": True}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        repo_link = response.json().get("html_url")
        return f"Rᴇᴘᴏsɪᴛᴏʀʏ ᴄʀᴇᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!\nYᴏᴜʀ ʀᴇᴘᴏ ʟɪɴᴋ: {repo_link}"
    else:
        return f"Failed to create repository. Error: {response.text}"

@Client.on_message(filters.command("create_repo", prefixes="/") & filters.user(ADMINS))
#@app.on_message(filters.command("create_repo", prefixes="/"))
def create_repo_command(client, message):
    command_parts = message.text.split(" ", 1)

    if len(command_parts) == 2:
        repo_name = command_parts[1].strip()
        response_text = create_github_repo(repo_name)
        message.reply_text(response_text)
    else:
        message.reply_text("Iɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ᴜsᴀɢᴇ. Pʟᴇᴀsᴇ ᴜsᴇ /create_repo <repository_name>")


@Client.on_message(filters.command(["gitpublic"]) & filters.user(ADMINS))
# @Client.on_message(filters.command(["gitprivate", "gitpublic"]))
def change_repo_public(client, message):
    try:
        # Ensure that only the owner can use these commands
#        if message.from_user.id != ADMINS:
#        message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ")
#            return

        # Extracting GitHub repository URL from the command
        url = message.text.split(" ", 1)[1].strip()

        # Assuming the URL is in the format 'https://github.com/user/repo'
        parts = url.split("/")
        username, repo_name = parts[-2], parts[-1]

        # Replace 'YOUR_GITHUB_TOKEN' with your GitHub token
        headers = {"Authorization": f"token {github_token}"}

        # Determine whether to set the repository to private or public
        is_private = True if message.command[0] == "gitprivate" else False

        # Change repository visibility using GitHub API
        response = requests.patch(f"https://api.github.com/repos/{username}/{repo_name}", json={"private": is_private}, headers=headers)

        if response.status_code == 200:
            visibility_status = "private" if is_private else "public"
            message.reply_text(f"Repository {username}/{repo_name} set to {visibility_status}.")
            message.reply_text(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ.....")
        else:
            message.reply_text(f"Fᴀɪʟᴇᴅ ᴛᴏ sᴇᴛ ʀᴇᴘᴏsɪᴛᴏʀʏ ᴠɪsɪʙɪʟɪᴛʏ. Sᴛᴀᴛᴜs ᴄᴏᴅᴇ: {response.status_code}")

    except IndexError:
        message.reply_text(f"Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ URL ᴀғᴛᴇʀ ᴛʜᴇ /{message.command[0]} command.")
    except Exception as e:
        message.reply_text(f"An error occurred: {str(e)}")





@Client.on_message(filters.command(["gitprivate"]) & filters.user(ADMINS))
# @Client.on_message(filters.command(["gitprivate", "gitpublic"]))
def change_repo_private(client, message):
    try:
        # Ensure that only the owner can use these commands
#        if message.from_user.id != ADMINS:
#        message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ")
#            return

        # Extracting GitHub repository URL from the command
        url = message.text.split(" ", 1)[1].strip()

        # Assuming the URL is in the format 'https://github.com/user/repo'
        parts = url.split("/")
        username, repo_name = parts[-2], parts[-1]

        # Replace 'YOUR_GITHUB_TOKEN' with your GitHub token
        headers = {"Authorization": f"token {github_token}"}

        # Determine whether to set the repository to private or public
        is_private = True if message.command[0] == "gitprivate" else True

        # Change repository visibility using GitHub API
        response = requests.patch(f"https://api.github.com/repos/{username}/{repo_name}", json={"private": is_private}, headers=headers)

        if response.status_code == 200:
            visibility_status = "private" if is_private else "public"
            message.reply_text(f"Repository {username}/{repo_name} set to {visibility_status}.")
            message.reply_text(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ.....")
        else:
            message.reply_text(f"Fᴀɪʟᴇᴅ ᴛᴏ sᴇᴛ ʀᴇᴘᴏsɪᴛᴏʀʏ ᴠɪsɪʙɪʟɪᴛʏ. Sᴛᴀᴛᴜs ᴄᴏᴅᴇ: {response.status_code}")

    except IndexError:
        message.reply_text(f"Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ URL ᴀғᴛᴇʀ ᴛʜᴇ /{message.command[0]} command.")
    except Exception as e:
        message.reply_text(f"An error occurred: {str(e)}")
                
