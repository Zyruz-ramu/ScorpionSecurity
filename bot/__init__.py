import os
import time
import asyncio
from bot.Config import Var
from telethon.sessions import StringSession

from telethon import TelegramClient 

if Var.STRING_SESSION:

    session_name = str(Var.STRING_SESSION)

    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)

else:

    session_name = "startup"

    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)

CMD_HNDLR = Var.CMD_HNDLR
