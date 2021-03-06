from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import sudo_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""b> ๐ช ** ูุฑุญุจูุง {message.from_user.first_name} ** \ n
๐ช ** [{BOT_NAME}] (https://t.me/ {BOT_USERNAME}) ูุชูุญ ูู ุชุดุบูู ุงูููุณููู ูู ูุฌููุนุงุช ูู ุฎูุงู ุงูุฏุฑุฏุดุงุช ุงูุตูุชูุฉ ุงูุฌุฏูุฏุฉ ูู Telegram! **

๐ธ ** ุงูุชุดู ุฌููุน ุฃูุงูุฑ ุงูุฑูุจูุช ูููููุฉ ุนูููุง ูู ุฎูุงู ุงูููุฑ ุนูู ุฒุฑ ยป๐ ุงูุฃูุงูุฑ! **

 **ููุนุฑูุฉ ููููุฉ ุงุณุชุฎุฏุงู ูุฐุง ุงูุฑูุจูุช ุ ูุฑุฌู ุงูููุฑ ููู ยป๐ผ๏ธุฏููู ุงูุงุณุชุฎุฏุงู! **
</ b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "๐ฏ๏ธ ุฃุถููู ุฅูู ูุฌููุนุชู", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "๐ผ๏ธุฏููู ุงูุงุณุชุฎุฏุงู", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "๐ ุงูุฃูุงูุฑ", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "ุตูุงุญุจ ุงููุจูุช โฉ", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "ุฌูุฑูุจ ุงูุฏุนูู", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "ูููุงู ุงูุฏุนูู", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""โ ** ุงูุฑูุจูุช ููุฏ ุงูุชุดุบูู ** \ n <b> ๐? ** ููุช ุงูุชุดุบูู: ** </ b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ุฌูุฑูุจ ุงูุฏุนูู", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "ูููุงู ุงูุฏุนูู", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b> ๐๐ป ** ูุฑุญุจูุง ** {message.from_user.mention ()} </b>


**ูุฑุฌู ุงูุถุบุท ุนูู ุงูุฒุฑ ุฃุฏูุงู ููุฑุงุกุฉ ุงูุดุฑุญ ูุงูุงุทูุงุน ุนูู ูุงุฆูุฉ ุงูุฃูุงูุฑ ุงููุชุงุญุฉ!**

๐ช""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ุดุฑุญ ุงูุงุณุชุฎุฏุงู", callback_data="cbguide"
                    )
                ]
            ]
        ),
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b> ๐ธ ูุฑุญุจูุง {message.from_user.mention} ูุฑุญุจูุง ุจู ูู ูุงุฆูุฉ ุงููุณุงุนุฏุฉ! </ b>

**ูู ูุฐู ุงููุงุฆูุฉ ุ ููููู ูุชุญ ุงูุนุฏูุฏ ูู ููุงุฆู ุงูุฃูุงูุฑ ุงููุชุงุญุฉ ุ ููู ูู ูุงุฆูุฉ ุฃูุงูุฑ ููุฌุฏ ุฃูุถูุง ุดุฑุญ ููุฌุฒ ููู ุฃูุฑ**

๐ช""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ุงูุงูุงููุฑ ุงูุงุณูุงุณููู ๐", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "ุงูุงูุงููุฑ ุงููููุชูุฏูู ๐", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ุงูุงููุฑ ุงูุงุฏูููููู ๐", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "ุงูุงููุฑ ุงููููุทูุฑ ๐", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ุงูุงููุฑ ุงููููุงููู ๐", callback_data="cbowner"
                    )
                ],
                
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "๐ `PONG!!`\n"
        f"๐ธ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "๐ธ ุญุงูุฉ ุงูุจูุช: \ n"
        f"โข *ูุฏุฉ ุงูุชุดุบูู:** `{uptime}`\n"
        f"โข ** ููุช ุงูุจุฏุก: ** `{START_TIME_ISO}`"
    )
