# FOR OUTGOING MESSAGES 
# BY @Alone_loverboy 
# MESSAGE FORWARD TO SENDER

"""

Outgoing Message(s) Forwarder (•﹏•)

"""
from telethon import events 
from bot import bot

from . import *

@bot.on(events.NewMessage(func=lambda e: e.is_private))
async def out_going_message(event):
  
    s = await event.get_reply_message()
    
    if s is None:

        return

    to_send = event.raw_text

    who = event.sender_id

    if s.fwd_from:

        to_user = s.fwd_from.sender_id.user_id
        
    else:

        return

    if who == OWNER_ID:

        if to_send.startswith("/"):

            return

        if event.text is not None and event.media:

            # if sending media

            bot_api_file_id = pack_bot_file_id(event.media)

            await asst.send_file(

                to_user,

                file=bot_api_file_id,

                caption=event.text,

                reply_to=x.reply_to_msg_id,

            )

        else:

            await asst.send_message(to_user, to_send, reply_to=x.reply_to_msg_id)
