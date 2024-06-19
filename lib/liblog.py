# Copyright (c) 2024, Bruno Monteiro
# All rights reserved.
#
"""
A simple logging library.

This library provides a simple wrapper around Python's built-in logging module.
It provides a single class `liblog` that can be used to configure the logging
module and log messages.
"""
import logging

class liblog:
    """
    A simple wrapper for Python's built-in logging module.

    This class provides a simple interface for configuring the logging module
    and logging messages.

    Attributes:
        filename (str): The name of the log file. Default is 'default.log'.
        level (int): The logging level. Default is logging.INFO.
    """
    def __init__(self, filename='logs/default.log', level=logging.INFO):
        """
        Initialize a new instance of liblog.

        Args:
            filename (str): The name of the log file. Default is 'default.log'.
            level (int): The logging level. Default is logging.INFO.
        """
        logging.basicConfig(filename=filename, level=level)

    def info(self, message):
        """
        Log an info message.

        Args:
            message (str): The message to log.
        """
        logging.info(message)

    def warning(self, message):
        """
        Log a warning message.

        Args:
            message (str): The message to log.
        """
        logging.warning(message)

    def error(self, message):
        """
        Log an error message.

        Args:
            message (str): The message to log.
        """
        logging.error(message)

    def critical(self, message):
        """
        Log a critical message.

        Args:
            message (str): The message to log.
        """
        logging.critical(message)

log = liblog()

