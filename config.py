import os
from os import getenv

from dotenv import load_dotenv

from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Xavier Music")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/fe6541376a6e024356600.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/fe6541376a6e024356600.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/fe6541376a6e024356600.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/fe6541376a6e024356600.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "OxMusicxO_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "E_J_W")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "O_A_V")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "K_P_S_6")

OWNER_NAME = getenv("OWNER_NAME", "W_Q_Z")

OWNER_ID = int(os.environ.get("OWNER_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/")
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
