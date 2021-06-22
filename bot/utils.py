import sys
import math
from bot import bot
from telethon import events
from pathlib import Path
from bot.Config import Var, Config
import logging
import inspect

def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import bot.utils
        import importlib
        path = Path(f"bot/security/{shortname}.py")
        name = "bot.security.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Successfully (re)imported " + shortname)
    else:
        import bot.utils
        import importlib
        path = Path(f"bot/security/{shortname}.py")
        name = "bot.security.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.tgbot = bot.tgbot
        mod.Var = Var
        mod.command = command
        mod.logger = logging.getLogger(shortname)

def start_mybot(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"bot/assistant/{shortname}.py")
        name = "bot.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Initialising TGBot.")
        print("TGBot - Imported " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"bot/assistant/{shortname}.py")
        name = "bot.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        spec.loader.exec_module(mod)
        sys.modules["bot.assistant" + shortname] = mod
        print("TGBot Has imported " + shortname)


def load_pmbot(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"bot/assistant/pmbot/{shortname}.py")
        name = "bot.assistant.pmbot.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Initialising PMBot.")
        print("PMBot - Imported " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path

        path = Path(f"bot/assistant/pmbot/{shortname}.py")
        name = "bot.assistant.pmbot.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        spec.loader.exec_module(mod)
        sys.modules["bot.assistant.pmbot." + shortname] = mod
        print("PMBot Has imported " + shortname)