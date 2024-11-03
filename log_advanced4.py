"""
Send logs to Papertrail Log Management System
"""

import logging
from logging.handlers import SysLogHandler
import time

PAPERTRAIL_HOST = "logs3.papertrailapp.com" # Change the Host
PAPERTRAIL_PORT = 17313 # Change the Port

logger=logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

handler=SysLogHandler(address=(PAPERTRAIL_HOST,PAPERTRAIL_PORT))

format=logging.Formatter(fmt='%(levelname)s|%(module)s|%(funcName)s|Line:%(lineno)d] %(asctime)s: %(message)s',datefmt='%Y-%m-%dT%H:%M:%S%z')

handler.setFormatter(format)

logger.addHandler(handler)


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