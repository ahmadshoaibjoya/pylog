import logging
import logging.handlers
import queue

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


# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.error('This is an error message')


print("This message comes before log message => :) Hello Berlin")
# ==================================
# Print the content of the log Queue
for element in list(log_queue.queue):
    print(element)
# ==================================

# Stop the listener once logging is done
listener.stop()
