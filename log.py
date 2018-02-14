#!/usr/bin/python

import os
import logging
#from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

diamond_back_home = os.path.expanduser(os.path.join('~/.config', 'diamondback'))
diamond_back_log = diamond_back_home + "/" + "dback.log"

'''
def log_setup():
    logger = logging.getLogger("DiamondBack")
    logger.setLevel(logging.DEBUG)

    hdlr = TimedRotatingFileHandler(diamond_back_log,when="D",interval=30,backupCount=30)

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    hdlr.setFormatter(formatter)

    logger.addHandler(hdlr)

    return logger
'''

def log_setup():

    logger = logging.getLogger("DiamondBack")
    logger.setLevel(logging.DEBUG)

    hdlr = WatchedFileHanlder(diamond_back_log)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    hdlr.setFormatter(formatter)

    logger.addHandler(hdlr)

    return logger

if __name__ == "__main__":
   log_setup()
