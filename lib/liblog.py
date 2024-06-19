import logging

class liblog:
    def __init__(self, filename='default.log', level=logging.INFO):
        logging.basicConfig(filename=filename, level=level)

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)

    def critical(self, message):
        logging.critical(message)

log = liblog()
