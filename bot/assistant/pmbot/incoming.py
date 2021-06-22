# FOR INCOMING MESSAGES 
# BY @Alone_loverboy 
# MESSAGE FORWARD TO OWNER

"""

Incoming Message(s) Forwarder. ⊙﹏⊙

"""
from telethon import events 
from dmbot import tgbot

from . import *

# if incoming message

@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def new_message(event):
  
    imcoming = event.raw_text
    
    who = event.sender_id
    
    if is_blacklisted(who):

        return

    # NO NEED TO REPLY TO BLOCKED USER anymore

    if incoming.startswith("/"):

        pass

    elif who == OWNER_ID:

        return

    else:
        await event.forward_to(OWNER_ID)
        
  # BY @Alone_loverboy (◍•ᴗ•◍)
  # Don't try to steal credit else gay🥱
  # MY PERSONAL BOT
  # ANDI MANDI RANDI KANGERS KI MAA KI RANDI😛😝.
  # MY PERSON BOT
