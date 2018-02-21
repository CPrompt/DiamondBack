#!/usr/bin/python

import os
import logging
from logging.handlers import WatchedFileHandler

diamond_back_home = os.path.expanduser(os.path.join('~/.config', 'diamondback'))
diamond_back_log = diamond_back_home + "/" + "dback.log"

def log_setup():

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    hdlr = WatchedFileHandler(diamond_back_log)
    formatter = logging.Formatter("[%(filename)s:%(lineno)s - %(funcName)20s()] %(asctime)s %(levelname)s %(message)s") 
    hdlr.setFormatter(formatter)

    logger.addHandler(hdlr)

    return logger

if __name__ == "__main__":
   log_setup()
