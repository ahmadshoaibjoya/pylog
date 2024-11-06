"""
In this script a multi-destination (console, log file, external service) and non-blocking (using QueueHandler and QueueListener) logging are implemented.
Also the log level filter is implemented
"""
import logging
from logging.handlers import SysLogHandler
import queue
import atexit

class AppLogger():
    def __init__(self) -> None:

        self.log_queue=queue.Queue()
        # Create the QueueHandler
        self.queue_handler=logging.handlers.QueueHandler(self.log_queue)
        
        # Create logger for the program
        self.logger=logging.getLogger('my_app')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(self.queue_handler)


        self.stream_format=logging.Formatter('[%(levelname)s|%(module)s|L%(lineno)d] => %(message)s')
        # Handler 1: Display logs in console
        self.stream_handler=logging.StreamHandler()
        self.stream_handler.setLevel(logging.DEBUG)
        self.stream_handler.setFormatter(self.stream_format)
        # Logs with ERROR and CRITICAL levels are filtered and will not be displayed console.
        self.stream_handler.addFilter(MyLevelFilter([40, 50]))


        self.file_format=logging.Formatter(fmt='[%(levelname)s|%(module)s|L%(lineno)d] %(asctime)s: %(message)s', datefmt='%Y-%m-%dT%H:%M:%S%z')
        # Handler 2: Store logs in a log file
        self.file_handler=logging.FileHandler('logs/app.log')
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(self.file_format)
        # Logs with DEBUG, INFO, WARNING levels are filtered and will not be stored in log file.
        self.file_handler.addFilter(MyLevelFilter([10, 20, 30]))


        self.syslog_format=logging.Formatter('[%(module)s|L%(lineno)d] => %(message)s')
        # Handler 3: Send logs to external an servcie (Papertrail Log Management System)
        PAPERTRAIL_HOST = "logsN.papertrailapp.com" # Change the Host
        PAPERTRAIL_PORT = 4444 # Change the Port
        self.syslog_hander=SysLogHandler(address=(PAPERTRAIL_HOST,PAPERTRAIL_PORT))
        self.syslog_hander.setLevel(logging.DEBUG)
        self.syslog_hander.setFormatter(self.syslog_format)

        # Create the QueueListener
        self.queue_listener=logging.handlers.QueueListener(self.log_queue, self.stream_handler, self.file_handler, self.syslog_hander, respect_handler_level= True)
        # Start the listener
        self.queue_listener.start()
        # When program normaly terminates, stop the listener
        atexit.register(self.queue_listener.stop)


    def get_logger(self):
        return self.logger


# My log filtering class
class MyLevelFilter(logging.Filter):
    """
    This filter allows log messages with log levels (DEBAG,INFO, WARNING) to be displayed in console and
    allows log messages with log levels (ERROR, CRITICAL) to be stored in the log file.
    """
    def __init__(self, level_no: list) -> None:
        super().__init__()
        self.level_no=level_no
        
    def filter(self, record: logging.LogRecord) -> bool:      
        return record.levelno not in self.level_no



    
app_logger=AppLogger()
logger=app_logger.get_logger() # The 'logger' global variable is now importable directly










# if __name__=='__main__':
#     app_logger=AppLogger()
#     logger=app_logger.get_logger()
#     logger.debug("debug message...")
#     logger.info("info message...")
#     logger.warning("warning message...")
#     logger.error("error message...")
#     logger.critical("critical message...")

   
    