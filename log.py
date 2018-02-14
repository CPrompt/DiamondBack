#!/usr/bin/python

import logging
import os
from logging.handlers import TimedRotatingFileHandler

diamond_back_home = os.path.expanduser(os.path.join('~/.config', 'diamondback'))
diamond_back_log = diamond_back_home + "/" + "dback.log"

def log_setup():

    logger = logging.getLogger("DiamondBack")
    logger.setLevel(logging.DEBUG)
    
    hdlr = TimedRotatingFileHandler(diamond_back_log,when="D",interval=30,backupCount=30)

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    hdlr.setFormatter(formatter)
    
    logger.addHandler(hdlr)

    return logger

