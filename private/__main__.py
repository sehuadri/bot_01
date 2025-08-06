from private import *
from importlib import import_module
from private.modules import ALL_MODULES
for module_name in ALL_MODULES:
        imported_module = import_module("private.modules." + module_name)
bot.run_until_disconnected()

usr.local.bin

