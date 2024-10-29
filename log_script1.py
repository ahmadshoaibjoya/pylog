import logging
import logging.config
import json

myLogger=logging.getLogger("my_app")

# Converts the json file to python dictionary
with open("log_config.json", "r") as f:
    config = json.load(f)
# Adds the config dictionary to log configuration
logging.config.dictConfig(config)

myLogger.warning("Program starts...")

try:
    print(1/0)
except:
    myLogger.exception("There is an exception:")