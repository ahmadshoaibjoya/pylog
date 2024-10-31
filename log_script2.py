"""
The filters are configured in a config file.
"""
import logging
import logging.config
import json


class MyLevelFilter(logging.Filter):
    """
    This filter allows log messages with log levels (DEBAG,INFO, WARNING) to be displayed in console and
    allows log messages with log levels (ERROR, CRITICAL) to be stored in the log file.
    """
    def __init__(self, level_no: int) -> None:
        super().__init__()
        self.level_no=level_no
        
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelno not in self.level_no


with open("configs/log_config2.json", "r") as file:
    config = json.load(file)
logging.config.dictConfig(config)

logger=logging.getLogger("my_app")


logger.debug("debug message. level number: 10")
logger.info("info message. level number: 20")
logger.warning("warning message. level number: 30")
logger.error("error message. level number: 40")
logger.exception("exception message...")
logger.critical("critical message. level number: 50")


