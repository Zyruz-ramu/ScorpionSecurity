import os
from telethon.tl.types import ChatBannedRights

class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    DM_TEXT = os.environ.get("DM_TEXT", None)
    PM_PIC = os.environ.get("PM_PIC", None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)
    OWNER_ID = str(int(x) for x in os.environ.get(
            "OWNER_ID",
            "719195224").split())
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    PMSECURITY = os.environ.get("PMSECURITY", "on") 
    DB_URI = os.environ.get("DATABASE_URL", None)
    LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    CMD_HNDLR = os.environ.get("CMD_HNDLR", r"\.")
    MAX_SPAM = int(os.environ.get("MAX_SPAM", ""))
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
    if PRIVATE_GROUP_ID is not None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers.")
                
class Development(Var):
    LOGGER = True
    # Here for later purposes
