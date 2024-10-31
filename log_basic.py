"""
A basic logging setup
"""
import logging.handlers
import requests
import logging
import time

logging.basicConfig(
    filename='logs/app.log',
    level=logging.DEBUG, 
    format='%(asctime)s - Logger Name: %(name)s - File Name: %(module)s - Function Name:%(funcName)s - %(levelname)s - %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S'
    )


log=logging.getLogger("my_module")

def open_url():
    url = "Http://www.google.com"
    response = requests.request("GET", url)
    log.info("Function is invoked...")
    log.exception("An Exception is happened...")


log.debug("The program is running...")
log.info("The request sent...")
log.warning("Close the program...")
log.error("There is an error...")
log.critical("Something is happened...")

print("Program is running...")
for _ in range(10):
    open_url()
    time.sleep(3)



# ================================
"""
    Formatter instances are used to convert a LogRecord to text.

    Formatters need to know how a LogRecord is constructed. They are
    responsible for converting a LogRecord to (usually) a string which can
    be interpreted by either a human or an external system. The base Formatter
    allows a formatting string to be specified. If none is supplied, the
    style-dependent default value, "%(message)s", "{message}", or
    "${message}", is used.

    The Formatter can be initialized with a format string which makes use of
    knowledge of the LogRecord attributes - e.g. the default value mentioned
    above makes use of the fact that the user's message and arguments are pre-
    formatted into a LogRecord's message attribute. Currently, the useful
    attributes in a LogRecord are described by:

    %(name)s            Name of the logger (logging channel)
    %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                        WARNING, ERROR, CRITICAL)
    %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                        "WARNING", "ERROR", "CRITICAL")
    %(pathname)s        Full pathname of the source file where the logging
                        call was issued (if available)
    %(filename)s        Filename portion of pathname
    %(module)s          Module (name portion of filename)
    %(lineno)d          Source line number where the logging call was issued
                        (if available)
    %(funcName)s        Function name
    %(created)f         Time when the LogRecord was created (time.time()
                        return value)
    %(asctime)s         Textual time when the LogRecord was created
    %(msecs)d           Millisecond portion of the creation time
    %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                        relative to the time the logging module was loaded
                        (typically at application startup time)
    %(thread)d          Thread ID (if available)
    %(threadName)s      Thread name (if available)
    %(process)d         Process ID (if available)
    %(message)s         The result of record.getMessage(), computed just as
                        the record is emitted
    """
