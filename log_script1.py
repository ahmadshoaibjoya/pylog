"""
Configure logging in a Json file and use logging.config.
There are two StreamHandler and FileHandler in the Json config file.
"""

import logging
import logging.config
import json

myLogger=logging.getLogger("my_app")

# Converts the json config file to python dictionary
with open("configs/log_config1.json", "r") as f:
    config = json.load(f)
# Adds the config dictionary to log configuration
logging.config.dictConfig(config)

myLogger.warning("Program starts...")

try:
    print(1/0)
except:
    myLogger.exception("There is an exception:")