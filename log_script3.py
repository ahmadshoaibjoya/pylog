"""
Send logs to Papertrail Log Management System, using config file.
"""

import logging
import logging.config
import json
import time

with open("configs/log_config3.json","r") as file:
    config=json.load(file)

logging.config.dictConfig(config)
logger=logging.getLogger("my_app")


for _ in range(20):
    logger.debug("debug message...")
    time.sleep(1)
    logger.info("info message...")
    time.sleep(1)
    logger.warning("warning message...")
    time.sleep(1)
    logger.error("error message...")
    time.sleep(1)
    logger.exception("exception message...")
    time.sleep(1)
    logger.critical("critical message...")
    time.sleep(1)