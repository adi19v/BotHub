<<<<<<< HEAD
"""AFK Plugin for @UniBorg
Syntax: .afk REASON"""
import logging
import asyncio
import datetime
import time
from telethon import events
from telethon.tl import functions, types
from uniborg.util import time_formatter
=======
"""afkb Plugin for @UniBorg
Syntax: .afkb REASON"""
import asyncio
import datetime
import shutil 
import random, re
import time
from time import gmtime, strftime
from datetime import timedelta
from datetime import datetime
from telethon import events
from telethon.tl import functions, types
from uniborg.util import progress, is_read, humanbytes, time_formatter, admin_cmd
from sample_config import Config
from platform import python_version, uname
>>>>>>> b387c9f97040811fb15405edd4c526a7a01ee08a

# ================= CONSTANT =================
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================

<<<<<<< HEAD
global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
USER_AFK = {}
afk_time = {}
last_afk_message = {}


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  # pylint:disable=E0602
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "Set AFK mode to False"
=======
global USER_afkb  # pylint:disable=E0602
global afkb_time  # pylint:disable=E0602
global last_afkb_message  # pylint:disable=E0602
global afkb_since # pylint:disable=E0602
USER_afkb = {}
afkb_time = {}
last_afkb_message = {}
afkb_since = {}
# current_time = datetime.now().strftime(" Time: %H:%M:%S \n  Date: %d/%m/%y ")

@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afkb(event):
    global USER_afkb  # pylint:disable=E0602
    global afkb_time  # pylint:disable=E0602
    global last_afkb_message  # pylint:disable=E0602
    global afkb_since # pylint:disable=E0602
    current_message = event.message.message
    if ".afkb" not in current_message and "yes" in USER_afkb:  # pylint:disable=E0602
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "Set afk mode to False"
>>>>>>> b387c9f97040811fb15405edd4c526a7a01ee08a
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PRIVATE_GROUP_BOT_API_ID` " + \
                "for the proper functioning of afkb functionality " + \
                "in @UniBorg\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True
            )
<<<<<<< HEAD
        USER_AFK = {}  # pylint:disable=E0602
        afk_time = {}  # pylint:disable=E0602
=======
        USER_afkb = {}  # pylint:disable=E0602
        afkb_time = {}  # pylint:disable=E0602
        afkb_since = {}  # pylint:disable=E0602
>>>>>>> b387c9f97040811fb15405edd4c526a7a01ee08a


@borg.on(events.NewMessage(pattern=r"\.afkb ?(.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
<<<<<<< HEAD
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global reason
    USER_AFK = {}
    afk_time = {}
    last_afk_message = {}
    reason = event.pattern_match.group(1)
    if not USER_AFK:  # pylint:disable=E0602
=======
    global USER_afkb  # pylint:disable=E0602
    global afkb_time  # pylint:disable=E0602
    global last_afkb_message  # pylint:disable=E0602
    global reason
    global afkb_since # pylint:disable=E0602
    USER_afkb = {}
    afkb_time = {}
    last_afkb_message = {}
    afkb_since = {}
    reason = event.pattern_match.group(1)
    if not USER_afkb:  # pylint:disable=E0602
>>>>>>> b387c9f97040811fb15405edd4c526a7a01ee08a
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(
                types.InputPrivacyKeyStatusTimestamp()
            )
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
<<<<<<< HEAD
            afk_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_AFK = f"yes: {reason}"  # pylint:disable=E0602
        if reason:
            await event.edit(f"Set AFK mode to True, and Reason is {reason}")
=======
            afkb_time = datetime.now()  # pylint:disable=E0602
        USER_afkb = f"yes: {reason}"  # pylint:disable=E0602
        if reason:
            await event.edit(f"Set afk mode to True, and Reason is {reason}")
>>>>>>> b387c9f97040811fb15405edd4c526a7a01ee08a
        else:
            await event.edit(f"Set afk mode to True")
        await asyncio.sleep(5)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                f"Set afk mode to True, and Reason is {reason}"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


@borg.on(events.NewMessage(  # pylint:disable=E0602
    incoming=True,
    func=lambda e: bool(e.mentioned or e.is_private)
))
async def on_afkb(event):
    if event.fwd_from:
        return
<<<<<<< HEAD
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    afk_since = "**a while ago**"
=======
    global USER_afkb  # pylint:disable=E0602
    global afkb_time  # pylint:disable=E0602
    global last_afkb_message  # pylint:disable=E0602
    global afkb_since # pylint:disable=E0602
    afkb_since = "**A While Ago**"
>>>>>>> b387c9f97040811fb15405edd4c526a7a01ee08a
    current_message_text = event.message.message.lower()
    if "afkb" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
<<<<<<< HEAD
    if USER_AFK and not (await event.get_sender()).bot:  # pylint:disable=E0602
        if afk_time:  # pylint:disable=E0602
            now = datetime.datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
=======
    if USER_afkb and not (await event.get_sender()).bot:  # pylint:disable=E0602
        if afkb_time :  # pylint:disable=E0602
            now = datetime.now()
            datime_since_afkb = now - afkb_time  # pylint:disable=E0602
            time = float(datime_since_afkb.seconds)
>>>>>>> b387c9f97040811fb15405edd4c526a7a01ee08a
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afkb_since = "**Yesterday**"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afkb_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afkb_since = wday.strftime('%A')
            elif hours > 1:
                afkb_since = f"`{int(hours)}h{int(minutes)}m` **ago**"
            elif minutes > 0:
                afkb_since = f"`{int(minutes)}m{int(seconds)}s` **ago**"
            else:
                afkb_since = f"`{int(seconds)}s` **ago**"
        msg = None
<<<<<<< HEAD
        message_to_reply = f"My Master **3Cube** Is **AFK since** {afk_time} " + \
            f"\n\n__I don't promise that HE will be back within few hours__\n\n**Because my King is** {reason}" \
            if reason \
            else f"My King **3Cube** is **AFK Since** {afk_time} so wait until HE is back.\n\n**THANKS**"
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602
=======
        message_to_reply = f"My Master {DEFAULTUSER} Is **afk since** {afkb_since}" + \
            f"\n\n__and HE may be back soon__\n\n**Because my King is** {reason}" \
            if reason \
            else f"My King 👑 {DEFAULTUSER} 👑 is **afk Since** {afkb_since} so wait until He is back.\n\n**THANKS**."
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_afkb_message:  # pylint:disable=E0602
            await last_afkb_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afkb_message[event.chat_id] = msg  # pylint:disable=E0602
>>>>>>> b387c9f97040811fb15405edd4c526a7a01ee08a
