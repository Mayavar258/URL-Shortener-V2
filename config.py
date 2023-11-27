import os

from dotenv import load_dotenv

load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Mandatory variables for the bot to start
# API ID from https://my.telegram.org/auth
API_ID = "1522127"
# API Hash from https://my.telegram.org/auth
API_HASH = "1252ffe16baf341bfd7236f92df76b0e"
BOT_TOKEN = "6784231545:AAFqabbwfT8Vb34-pgs6RZZ5V-jgJJMRI28" # Bot token from @BotFather
ADMINS = ([int(i.strip()) for i in os.environ.get("ADMINS").split("1951205538")]
    if os.environ.get("ADMINS")
    else []
)

DATABASE_NAME = os.environ.get("DATABASE_NAME", "MdiskConvertor")
DATABASE_URL = "mongodb+srv://Cluster0:AMRKS@cluster0.6sxfz9f.mongodb.net/?retryWrites=true&w=majority"  # mongodb uri from https://www.mongodb.com/
OWNER_ID = "1951205538"  # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

#  Optionnal variables
LOG_CHANNEL = "-1002117005762"
UPDATE_CHANNEL = "ANLINKS_IN" # For Force Subscription
BROADCAST_AS_COPY = is_enabled((os.environ.get("BROADCAST_AS_COPY", "False")), False
)  # true if forward should be avoided
IS_PRIVATE = is_enabled(
    os.environ.get("IS_PRIVATE", "False"), "False"
)  # true for private use and restricting users
SOURCE_CODE = os.environ.get(
    "SOURCE_CODE", "https://github.com/mayavar258/URL-Shortener-V2"
)  # for upstream repo
# image when someone hit /start
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", "https://telegra.ph/file/e6706b0526df51784f349.jpg")
LINK_BYPASS = is_enabled(
    (os.environ.get("LINK_BYPASS", "False")), False
)  # if true, urls will be bypassed
# your shortener site domain
BASE_SITE = os.environ.get("BASE_SITE", "anlinks.in")

# For Admin use
CHANNELS = is_enabled((os.environ.get("CHANNELS", "True")), True)
CHANNEL_ID = (
    [int(i.strip()) for i in os.environ.get("CHANNEL_ID").split(" ")]
    if os.environ.get("CHANNEL_ID")
    else []
)

DE_BYPASS = (
    [i.strip() for i in os.environ.get("DE_BYPASS").split(",")]
    if os.environ.get("DE_BYPASS")
    else []
)
DE_BYPASS.append("mdisk.me")

FORWARD_MESSAGE = is_enabled(
    (os.environ.get("FORWARD_MESSAGE", "False")), False
)  # true if forwardd message to converted by reposting the post


WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "240"))
PORT = int(os.environ.get("PORT", "8000"))
