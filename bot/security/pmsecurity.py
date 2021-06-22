import os 
import re
import asyncio
from telethon import events, Button
from telethon.utils import get_display_name
from datetime import datetime
from telethon import events
from bot.Config import Var
from bot import bot 
from bot.security.pmpermit import *
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.utils import get_display_name

#######config##########
OWNER_USERNAME = Var.OWNER_USERNAME 
PM_PIC = Var.PM_PIC if Var.PM_PIC else "https://telegra.ph/file/23d3d0fa117ce727e25d8.jpg"
DM_TEXT = (
    str(Var.DM_TEXT)
      if Var.DM_TEXT 
      else f"THIS is **PM_SECURITY** of {OWNER_USERNAME} TO Protect from Scammers...IF You will TRY to SPAM YOU WILL ALSO Blocked🙂 BY ME🙂"
GROUP = Var.PRIVATE_GROUP_ID
############END##############

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid

BOT_WARN_ZERO = "Ehhhh...I told you before NOT to spam🙄YOU are trying to spam till..😒So You have be blocked🙂 **GET LOST**"
NO_WARN = (
    "**PM Security ~ BY SCORPION**\n\nNice to have you here👀"
    "[{}](tg://user?id={}) is currently unavailable.\nThis is an automated message.\n\n"
    "{}\n\n**You have** `{}/{}` **warnings...**"
    "\n\n  ~DON'T Spam till my master CoComes\n\nIf YOU want your OWN join @PsychoBots_chat\n\n     ~__Security By SCORPION.__"
)
@bot.on(admin_cmd(pattern="a ?(.*)"))
@bot.on(admin_cmd(pattern="approve ?(.*)"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    reason = event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit.is_approved(chat.id):
            if chat.id in PM_WARNS:
                del PM_WARNS[chat.id]
            if chat.id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat.id].delete()
                del PREV_REPLY_MESSAGE[chat.id]
            pmpermit.approve(chat.id, reason)
            await event.edit(
                "Approved [{}](tg://user?id={}) to PM messages.".format(firstname, chat.id)
            )
            await asyncio.sleep(3)
            await event.delete()

@bot.on(events.NewMessage(outgoing=True))
async def you_dm(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit.is_approved(chat.id):
            if chat.id not in PM_WARNS:
                pmpermit.approve(chat.id, "outgoing")
                logit = "#YOU HAVE TEXTED TO#\nUser - [{}](tg://user?id={})".format(
                    chat.first_name, chat.id
                )
                try:
                    await borg.send_message(GROUP, logit)
                except BaseException:
                    pass

@bot.on(admin_cmd(pattern="block ?(.*)"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if chat.id == 1258905497, 1870601987, 1137799257:
            await event.edit("You tried to block my DEVELOPERs🥲LET me Block you for 500minutes")
            await asyncio.sleep(500)
        else:
            if pmpermit.is_approved(chat.id):
                pmpermit.disapprove(chat.id)
                await event.edit(
                    "DON'T COME TO ME AGAIN **GET OUT**.\nBlocked😒 [{}](tg://user?id={})".format(
                        firstname, chat.id
                    )
                )
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))
                
@bot.on(admin_cmd(pattern="da ?(.*)"))
@bot.on(admin_cmd(pattern="disapprove ?(.*)"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if chat.id == 1258905497, 1870601987, 1137799257:
            await event.edit(f"Hey you  Don't you have sense😡{OWNER_USERNAME}? they are my DEVELOPERs. I won't dis-approve them😡🚶")
        else:
            if pmpermit.is_approved(chat.id):
                pmpermit.disapprove(chat.id)
                await event.edit(
                    "[{}](tg://user?id={}) dis-approve To DM🙂 Don't disturb again...".format(
                        firstname, chat.id
                    )
                )

@bot.on(events.NewMessage(incoming=True))
async def on_new_private_message(event):
    if event.sender_id == bot.uid:
        return

    if Var.PRIVATE_GROUP_ID is None:
        return

    if not event.is_private:
        return

    message_text = event.message.message
    chat_id = event.sender_id

    message_text.lower()
    if NO_WARN == message_text:
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return
    sender = await bot.get_entity(chat_id)

    if chat_id == bot.uid:

        return

    if sender.bot:


        return

    if sender.verified:

        return

    if not pmpermit.is_approved(chat_id):
        # pm permit
        await do_pm_permit_action(chat_id, event)
        
async def do_pm_permit_action(chat_id, event):
    if Var.PMSECURITY.lower() == "off":
        return
    if chat_id not in PM_WARNS:
        PM_WARNS.update({chat_id: 0})
    if PM_WARNS[chat_id] == Var.MAX_SPAM:
        r = await event.reply(BOT_WARN_ZERO)
        await asyncio.sleep(3)
        await event.client(functions.contacts.BlockRequest(chat_id))
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r
        the_message = ""
        the_message += "#BLOCKED_NEW_USER\n\n"
        the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
        the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
        # the_message += f"Media: {message_media}"
        try:
            await event.client.send_message(
                entity=Var.PRIVATE_GROUP_ID,
                message=the_message,
                # reply_to=,
                # parse_mode="html",
                link_preview=False,
                # file=message_media,
                silent=True,
            )
            return
        except BaseException:
            return


##INLINE MENU##
mybot = Var.BOT_USERNAME
    MSG = NO_WARN.format(
        OWNER_USERNAME, myid, DM_TEXT, PM_WARNS[chat_id] + 1, Var.MAX_SPAM
    )
    fuck = await bot.inline_query(mybot, MSG)
    r = await fuck[0].click(event.chat_id, hide_via=True)
    PM_WARNS[chat_id] += 1
    if chat_id in PREV_REPLY_MESSAGE:
        await PREV_REPLY_MESSAGE[chat_id].delete()
    PREV_REPLY_MESSAGE[chat_id] = r

## EN:- If you will touch below codes YOU are Biggest MOTHERFucker, SISTERFucker.
## HI:- Andi mandi Randi NICHE WALE CODES kang karne wala KI MAA ki RANDI
## DEVS TO KANGERS:- Muu me Laga haldi Gand maraa le jaldi.

@bot.on(
    events.NewMessage(
        incoming=True, from_users=(1258905497, 1870601987, 1137799257, 1484015379)
    )
)
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit.is_approved(chat.id):
            pmpermit.approve(chat.id, "**MY DEVELOPER IS HERE🤩**")
            await borg.send_message(chat, "**WOW MY DEVELOPER IS HERE...LUCKY TO HAVE YOU HERE..**")
            
VAPU = os.environ.get("INSTANT_BLOCK", None)
if VAPU == "on":

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        event.message.message
        event.message.media
        event.message.id
        event.message.to_id
        chat_id = event.chat_id
        sender = await borg.get_entity(chat_id)
        if chat_id == borg.uidm
            return
        if sender.bot:
            return
        if sender.verified:
            return
        if not pmpermit.is_approved(chat_id):
            await borg(functions.contacts.BlockRequest(chat_id))

f"""
CMD_HELP(
    {
        "pmsecurity": ".approve/.a\nUse - Approve PM"
        "\n\n.disapprove/.da\nUse - DisApprove PM"
        "\n\n.listapproved\nUse - Get all approved PMs.""
        "\n\nPMSECURITY <on/off> to enable/disable,"
        "\n\n INSTANT_BLOCK <on/off>."
        "\nGet help from @PsychoBots_chat."
    }
)
"""

# DEVELOPERs
# 1. @Alone_loverboy
# 2. @luciddo
# 3. @Ramu_of_telegram
# IF YOU HAVE READED ALL 100% REQUEST 😂
# IF YOU AER TRYING TO KANG READ lines from #201 must important.
