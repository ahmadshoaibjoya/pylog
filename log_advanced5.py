"""
In this script for the purpose of Non-Blocking, the QueueHandler and QueueListener are implemented.
Non-Blocking: Log generation and handling can be decoupled, 
which prevents the main thread from being blocked by time-consuming log operations.
So the main application processes can continue without waiting for logs to be processed.

When an application has to handle a high volume of logging or 
when log operations involve potentially slow I/O (e.g., writing to disk or sending logs to an external service), 
QueueHandler and QueueListener help manage these operations asynchronously:
The main process or thread pushes log records to a queue using QueueHandler.
A separate thread or process runs a QueueListener that pulls log records from the queue 
and processes them using configured logging.Handler instances (e.g., FileHandler, StreamHandler).
"""

import logging
import logging.handlers
import queue
# atexit module allows to define multiple exit functions to be executed upon normal program termination
import atexit

# Create a queue
log_queue = queue.Queue()

# Set up a QueueHandler and add it to the logger
queue_handler = logging.handlers.QueueHandler(log_queue)

logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)
logger.addHandler(queue_handler)

# Create log message format
formatter = logging.Formatter('|%(levelname)s| - %(asctime)s - %(message)s')

# Create a handlers for the listener to write log records to a file
file_handler = logging.FileHandler('logs/app.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
# Create a handlers for the listener to print log records on console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)


# Set up a QueueListener
listener = logging.handlers.QueueListener(log_queue, file_handler, stream_handler)
listener.start()
# Stop the listener once the progam normaly terminates.
atexit.register(listener.stop)

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.error('This is an error message')


print("1 message => :) Hello Berlin")
print("2 message => :) Hello Berlin")
# ==================================
# Print the content of the log Queue, which are LogRecords
print("Queue content:")
for element in list(log_queue.queue):
    print(element)
# ==================================
print("3 message => :) Hello Berlin")
print("4 message => :) Hello Berlin")
print("5 message => :) Hello Berlin")
print("6 message => :) Hello Berlin")
print("7 message => :) Hello Berlin")
print("8 message => :) Hello Berlin")

# Stop the listener once logging is done
# listener.stop()
