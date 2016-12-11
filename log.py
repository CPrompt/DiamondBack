import logging
from logging.handlers import TimedRotatingFileHandler
import os

def log_setup():

    diamond_back_home = os.path.expanduser(os.path.join('~/.config', 'diamondback'))
    logger = logging.getLogger("DiamondBack")
    hdlr = TimedRotatingFileHandler(diamond_back_home + "/" + "dback.log",when = "D",interval = 30,backupCount = 30)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

    return logger
