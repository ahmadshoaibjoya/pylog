import logging
import logging.config
import json

myLogger=logging.getLogger("my_app")

with open("config.json", "r") as f:
    config = json.load(f)

logging.config.dictConfig(config)

myLogger.warning("Program starts...")

try:
    print(x)
except:
    myLogger.exception("There is an exception:")