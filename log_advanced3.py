"""
Filters in logging mechanism.
Filters are useful in cases where:
You want only certain types of messages logged (e.g., log only warnings related to a specific module).
You want to exclude specific messages (e.g., exclude debug messages from third-party libraries).
You need custom filtering that isn’t covered by log levels alone.
"""
import logging


class myFilter(logging.Filter):

    def __init__(self,value) -> None:
        self.filterValue=value
    
    # @override
    def filter(self, record: logging.LogRecord) -> bool:
        """
        Returns True if the *record* should be logged, or False otherwise.
        This function is called automatically, it is part of how Python’s logging mechanism works.
        """
        # Filter based on Level Name. Ex: logging.getLevelName(20) is INFO
        # return self.filterValue == record.levelname

        # Filter based on Level Number. Ex: INFO is 20
        # return self.filterValue == record.levelno

        # Filter based on Logger name
        # return self.filterValue == record.name
        
        # Filter based on module name
        # return self.filterValue == record.module
    
        # Filter based on message text
        # return self.filterValue == record.msg

        # Filter based on funcion name        
        return self.filterValue == record.funcName

        # Filter based on line number
        # return self.filterValue == record.lineno

        # Filter based on thread name
        # return self.filterValue == record.threadName
    
        # Filter based on file path
        # return self.filterValue == record.pathname



logger=logging.getLogger("my_app1")
logger.setLevel(logging.DEBUG)


consoleHander=logging.StreamHandler()
consoleHander.setLevel(logging.DEBUG)
format1=logging.Formatter("'%(asctime)s - %(levelname)s - %(message)s'")
consoleHander.setFormatter(format1)

# Add the created Filter to the Handler to filter records going to a specific destination (e.g., console or file).
consoleHander.addFilter(myFilter("subtraction")) # Filter based on funcion name

# # Add the created Filter Logger to filter records at the logger level before passing them to any handler.
# logger.addFilter(myFilter("subtraction"))


logger.addHandler(consoleHander)


logger.debug("debug message...")
logger.info("info message...")
logger.warning("warning message...")
logger.error("error message...")
logger.exception("exception message...")
logger.critical("critical message...")


def addition():
    logger.info("addition function is invoked.")
    return 2+2

def subtraction():
    logger.info("subtraction function is invoked.")
    return 2-2

addition()
subtraction()