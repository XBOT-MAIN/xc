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
        f"""b> 🎪 ** مرحبًا {message.from_user.first_name} ** \ n
🎪 ** [{BOT_NAME}] (https://t.me/ {BOT_USERNAME}) يتيح لك تشغيل الموسيقى في مجموعات من خلال الدردشات الصوتية الجديدة في Telegram! **

🎸 ** اكتشف جميع أوامر الروبوت وكيفية عملها من خلال النقر على زر »📚 الأوامر! **

 **لمعرفة كيفية استخدام هذا الروبوت ، يرجى النقر فوق »🗼︙دليل الاستخدام! **
</ b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🎯︙ أضفني إلى مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "🗼︙دليل الاستخدام", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "📚 الأوامر", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "صـاحب الـبوت ☩", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "جـروب الدعـم", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "قـناه الدعـم", url=f"https://t.me/{UPDATES_CHANNEL}")
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
        f"""✅ ** الروبوت قيد التشغيل ** \ n <b> 💠 ** وقت التشغيل: ** </ b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "جـروب الدعـم", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "قـناه الدعـم", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b> 👋🏻 ** مرحبًا ** {message.from_user.mention ()} </b>


**يرجى الضغط على الزر أدناه لقراءة الشرح والاطلاع على قائمة الأوامر المتاحة!**

🎪""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="شرح الاستخدام", callback_data="cbguide"
                    )
                ]
            ]
        ),
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b> 🎸 مرحبًا {message.from_user.mention} مرحبًا بك في قائمة المساعدة! </ b>

**في هذه القائمة ، يمكنك فتح العديد من قوائم الأوامر المتاحة ، وفي كل قائمة أوامر يوجد أيضًا شرح موجز لكل أمر**

🎪""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاوامـر الاسـاسـيه 🖇", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "الاوامـر الـمـتقدمه 🖇", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "اوامـر الادمـنيـه 🖇", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "اوامـر الـمـطور 🖇", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "اوامـر الـمـالـك 🖇", callback_data="cbowner"
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
        "🏓 `PONG!!`\n"
        f"🎸 `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🎸 حالة البوت: \ n"
        f"• *مدة التشغيل:** `{uptime}`\n"
        f"• ** وقت البدء: ** `{START_TIME_ISO}`"
    )
