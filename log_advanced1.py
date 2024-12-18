"""
Creates a Logger for the application and
adding one Handler to the Logger.
The Handler is StreamHandler
"""
import logging

# Creates a Logger
logger=logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Creates a Handler
# StreamHandler is for printing logs in console
handler1=logging.StreamHandler()
handler1.setLevel(logging.INFO)

# Creates log message format
simpleformat=logging.Formatter("'%(asctime)s - %(levelname)s - %(message)s'")
# Adds the created format to the Handler
handler1.setFormatter(simpleformat)

# Finally, adds the Handler to the created Logger
logger.addHandler(handler1)

logger.debug("debug message...")
logger.info("info message...")
logger.warning("warning message...")
logger.error("error message...")
logger.exception("exception message...")
logger.critical("critical message...")

