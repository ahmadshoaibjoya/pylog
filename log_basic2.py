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

logger.info("info message...")
logger.error("error message...")
logger.warning("warning message...")
logger.debug("debug message...")
logger.critical("critical message...")
logger.exception("exception message...")


