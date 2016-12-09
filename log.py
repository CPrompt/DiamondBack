import logging
from logging.handlers import TimedRotatingFileHandler

class monitor_log:

    def log_setup(self):
        logger = logging.getLogger("DiamondBack")
        #hdlr = logging.FileHandler("/home/curtis/.config/diamondback/dback.log")
        hdlr = TimedRotatingFileHandler("/home/curtis/.config/diamondback/dback.log",when = "D",interval = 30,backupCount = 30)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        logger.addHandler(hdlr)
        logger.setLevel(logging.DEBUG)

        return logger

