#!/usr/bin/python

import os
import time
import glob
import datetime
from datetime import date
import calendar
from read_json import output_config
from config import directory_of_backup
from log import log_setup

'''
import logging
from logging.handlers import WatchedFileHandler
diamond_back_home = os.path.expanduser(os.path.join('~/.config', 'diamondback'))
diamond_back_log = diamond_back_home + "/" + "dback.log"
'''

log_directory = directory_of_backup
old_logfiles = glob.glob(os.path.join(log_directory, '*.*'))

# current year and month
current_date = str.split(time.strftime("%Y %m"))
current_year = str.split(time.strftime("%Y"))
current_weekday = str.split(time.strftime("%d"))


# This section will take the current date and determine
# what day of the week was the first day (0 = Monday, 1 = Tuesday, etc...)
# Then it will tell how many days in the given month

def determine_last_day(this_date):
    current_calendar = calendar.monthrange(int(this_date[0]),int(this_date[1]))
    # we just need to return the number of days in this month
    return current_calendar[1]
'''
def log_setup():

    #logger = logging.getLogger("DiamondBack")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    hdlr = WatchedFileHandler(diamond_back_log)
    formatter = logging.Formatter("[%(filename)s:%(lineno)s - %(funcName)20s()] %(asctime)s %(levelname)s %(message)s") 
    hdlr.setFormatter(formatter)

    logger.addHandler(hdlr)

    return logger
'''

def remove_old_files():

    log_process = log_setup()
    message = ""

    current_day_in_month = int(current_weekday[0])
    days_in_month = determine_last_day(current_date)

    # list to hold the files found that are ready to be purged
    files_found = []

    for old_logs in old_logfiles:
        stat_info = os.stat(old_logs).st_mtime
        # change the st_mtime infor into a datestamp we can use better
        file_time_stamp = str(datetime.datetime.fromtimestamp(stat_info))
        time_split = str.split(file_time_stamp)[0]

        # This just splits the current date so we can parse it out
        dic_date = time_split.split("-")

        # we only want this to process on the last day of the month
        if(dic_date[0] == current_year):
            if(current_day_in_month == days_in_month):
                files_found.append(old_logs)
            else:
                message = "No Files"
                message = message + " : " + old_logs
        else:
            message = "All loops ended"
            '''
            # if the month of the file is the same as the current month
            if(int(dic_date[1]) == int(current_date[1])):
                # if the day of the log file is less than the last day of the month
                if(int(dic_date[2]) < int(days_in_month)):
                    # here we are going to try to delete records.
                    try:
                        #logger.info("Removing old files....")
                        files_found.append(old_logs)
                        # going to comment this out for testing
                        # os.remove(old_logs)
                    except:
                        logger.error("Could not remove files")
                else:
                    message = "First if"
            else:
                message = "Second if"
        else:
            message = "Third if " + old_logs
            '''

    if (len(files_found) == 0):
        print(message)
        log_process.info(message)
    else:
        print(message)
        log_process.warning("WARNING!")
        log_process.info(files_found)
    
    

if __name__ == "__main__":
    remove_old_files()






