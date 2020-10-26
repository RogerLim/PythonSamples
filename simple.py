#!/usr/bin/python3

import logging as logging

logger = logging.getLogger('dev')
logger.setLevel(logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
