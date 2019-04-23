"""This module contains implementation of GameofThrones logger class"""
import sys
import logging
from logging import handlers

class Logger():
    """
    Logger class to create logger
    """
    def __init__(self, log_file):
        """
        Constructor
        """
        self.log_file = log_file
        
    def configure_logger(self, logger_level):
        """
        Function to get logger object
        """
        logger = logging.getLogger('gameofthrones')
        level = logging.getLevelName(logger_level)
        logger.setLevel(level)

        if not logger.handlers:
            file_channel = handlers.\
                TimedRotatingFileHandler(self.log_file, when='midnight',
                                         interval=1)
            file_channel.setLevel(logger_level)
            stream_channel = logging.StreamHandler(sys.stdout)
            stream_channel.setLevel(logger_level)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - '
                                          '%(module)s:%(funcName)s' +
                                          ' - %(message)s')
            file_channel.setFormatter(formatter)
            stream_channel.setFormatter(formatter)
            logger.addHandler(file_channel)
            logger.addHandler(stream_channel)

        return logger