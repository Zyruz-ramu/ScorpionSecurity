import os
import time
import asyncio

from telethon.sessions import StringSession

from telethon import TelegramClient 

if Var.STRING_SESSION:

    session_name = str(Var.STRING_SESSION)

    bot = TelegramClient(StringSession(session_name), Var.API_ID, Var.API_HASH)

else:

    session_name = "startup"

    bot = TelegramClient(session_name, Var.API_ID, Var.API_HASH)
