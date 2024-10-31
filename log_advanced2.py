"""
Create a Logger for the application and
adding two Handlers to the Logger.
The Handlers are StreamHandler and FileHandler.
"""

import logging
import logging.handlers

# Creates a Logger
logger=logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# Creates a Handler
# Creates a Handler for printing logs in console
handler1=logging.StreamHandler()
handler1.setLevel(logging.INFO)

# Creates log message format
simpleFormat=logging.Formatter("'%(asctime)s - %(levelname)s - %(message)s'")
# Adds the created format to the Handler
handler1.setFormatter(simpleFormat)

# Finally, adds the Handler to the logger
logger.addHandler(handler1)
# =======================================
# Creates another Handler for storing logs in a log file
# handler2=logging.FileHandler('app.log')
# If the app.log file reaches to 1KB, another backup file will be created. It creates backups until 3 file.
handler2=logging.handlers.RotatingFileHandler('logs/app.log',maxBytes=1000,backupCount=3)
handler2.setLevel(logging.DEBUG)

# Creates log message format
detailedFormat=logging.Formatter('[%(levelname)s|%(module)s|%(funcName)s|Line:%(lineno)d] %(asctime)s: %(message)s')
# Sets the data and time format of the log message
detailedFormat.datefmt='%Y-%m-%dT%H:%M:%S%z'

# Adds the created format to the Handler
handler2.setFormatter(detailedFormat)

# Finally, adds the handler2 to the logger
logger.addHandler(handler2)

if __name__=="__main__":
    def my_function():
        logger.info("The function is invoked...")
        try:
            print(1/0)
        except:
            logger.exception("An exception is happened...")

    my_function()

    logger.info("The program finished.")


