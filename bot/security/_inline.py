import asyncio
import html
import os
import re
from math import ceil

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest

from bot import bot
from bot.Config import Var
###CONFIG###
PM_PIC = Var.PM_PIC if Var.PM_PIC else "https://telegra.ph/file/23d3d0fa117ce727e25d8.jpg"
OWNER_USERNAME = Var.OWNER_USERNAME
DM_TEXT = Var.DM_TEXT if Var.DM_TEXT else f"THIS is **PM_SECURITY** of {Var.OWNER_USERNAME} TO Protect from Scammers...IF You will TRY to SPAM YOU WILL ALSO Blocked🙂 BY ME🙂\n    ~__Security By SCORPION__~"
##END## :)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
mybot = Var.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
GROUP = Var.PRIVATE_GROUP_ID

BOT_WARN_ZERO = "Ehhhh...I told you before NOT to spam🙄YOU are trying to spam till..😒So You have be blocked🙂 **GET LOST**"

if Var.LOAD_MYBOT == "True":
    NO_WARN = (
        "**PM Security of [{}](tg://user?id={})**\n\n"
        "{}\n\n"
        "For immediate help, PM me via {}"
        "\nPlease choose why you are here, from the available options\n\n".format(PM_PIC, OWNER_USERNAME, myid, DM_TEXT, botname
        )
    )
elif Var.LOAD_MYBOT == "False":
    NO_WARN = (
        "**PM Security of [{}](tg://user?id={})**\n\n"
        "{}\n"
        "\nPlease choose why you are here, from the available options\n".format(PM_PIC, OWNER_USERNAME, myid, DM_TEXT
        )
    )

if Var.BOT_USERNAME is not None and bot is not None: 
      @bot.on(events.InlineQuery)
      async def inline_handler(event):
        builder = event.builder
        event.query.user_id == bot.uid and query.startswith("**PM"):
            TGBT = NO_WARN.format(OWNER_USERNAME, myid, DM_TEXT)
            result = builder.photo(
                file=PM_PIC,
                text=TGBT,
                Buttons=[
                [  
                  custom.Button.inline("To ask something😅", data="ask"),
                  custom.Button.inline("To Request 😓", data="req"),
                  custom.Button.inline("TO CHAT💬", data="chat"),
                  custom.Button.inline("SOMETHING else💢", data="elsee"),
                  custom.Button.inline("WHAT is This❔", data="know")]
                ],
            )

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ask")))
async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Ehhh😂This is not for you master"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"OK WHATEVER you want to ask you can ask to {OWNER_USERNAME} just wait some time👀\n\nTILL he will come online 🤧")
                target = await event.client(GetFullUserRequest(event.query.user_id))
        first_name = html.escape(target.user.first_name)
        love = event.query.user_id 
        if first_name is not None:
                first_name = first_name.replace("\u2060", "")
        tosend = f"Hey {OWNER_USERNAME}👀, [{first_name}](tg://user?id={love})  wants to ask something To you in PM."
        await bot.send_message(GROUP, tosend)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"req")))
async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Ehhh This is not for you master 😂"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Okay,You have some request to`{OWNER_USERNAME}`! He will help you😉!!\nTill then please **wait patienly and don't spam here.**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {OWNER_USERNAME}👀, [{first_name}](tg://user?id={ok})  wants to request something in PM!"
            await bot.send_message(GROUP, tosend)
            
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat")))
async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is not for you master😂"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"YOU WANT TO chat...ok 😉\nPlease wait and see if {OWNER_USERNAME} may know you he will reply soon!\nTill then, **do not spam.**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {OWNER_USERNAME}👀, [{first_name}](tg://user?id={ok}) He wants to talk in PM! for  **Chatting**!"
            await bot.send_message(GROUP, tosend)
            
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"elsee")))
async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Ehhh This is not for you master😂"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"ok😳You have something else for Master {OWNER_USERNAME} will glad to knwait**Till wait don't spam**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {OWNER_USERNAME}👀, [{first_name}](tg://user?id={ok}) wants to PM you He have **something else**😳!"
            await bot.send_message(GROUP, tosend)
            
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"know")))
async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Don't you know what is this😒lol"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(f"This is a PM_SECURITY service by @Psycho_Bots to protect My Master form Scammers..IF you also want to have PM_SECURITY service on Your telegram Account\n Contact to @PsychoBots_chat")
            
            
# Inline Buttons
# For SECURITY
