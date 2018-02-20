#!/usr/bin/python

import os
import time
import glob
import datetime
from datetime import date
import calendar
from read_json import output_config
from config import backupName, directory_of_backup, redundant_backup_directory, files_for_backup, ignored_files
from log import *

diamond_back_home = os.path.expanduser(os.path.join('~/.config', 'diamondback'))
logger = log_setup()
log_directory = directory_of_backup
old_logfiles = glob.glob(os.path.join(log_directory, '*.*'))


# current year and month
current_date = str.split(time.strftime("%Y %m"))
current_weekday = str.split(time.strftime("%d"))

# list to hold the files that will be deleted
files_found = []

# This section will take the current date and determine
# what day of the week was the first day (0 = Monday, 1 = Tuesday, etc...)
# Then it will tell how many days in the given month

def determine_last_day(this_date):
    current_calendar = calendar.monthrange(int(this_date[0]),int(this_date[1]))
    # we just need to return the number of days in this month
    return current_calendar[1]


def remove_old_files():

    current_day_in_month = int(current_weekday[0])
    days_in_month = determine_last_day(current_date)


    for old_logs in old_logfiles:
        stat_info = os.stat(old_logs).st_mtime
        # change the st_mtime infor into a datestamp we can use better
        file_time_stamp = str(datetime.datetime.fromtimestamp(stat_info))
        time_split = str.split(file_time_stamp)[0]

        # This just splits the current date so we can parse it out
        dic_date = time_split.split("-")

    if(current_day_in_month == days_in_month):
        if(int(dic_date[1] == int(current_date[1]))):
            if(int(dic_date[2]) < int(days_in_month)):
                try:
                    # os.remove(old_logs)
                    # any files found, add them to the list
                    files_found.append(old_logs)
                except:
                    logger.warning("Could not remove files!")
            else:
                files_found.count == 0
        else:
            files_found.count == 0
    else:
        files_found.count == 0


    if files_found.count == 0:
        logger.info("No files found to be removed")
    else:
        logger.info("Files remove : " + str(old_logs))


if __name__ == "__main__":
    remove_files()



