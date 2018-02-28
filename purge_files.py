#!/usr/bin/python

import os
import time
import glob
import datetime
from datetime import date
import calendar
from read_json import output_config
from config import directory_of_backup,outputFile
from yaml_log import configure_logger

log_directory = directory_of_backup
old_logfiles = glob.glob(os.path.join(log_directory, '*.*'))

alog = configure_logger('default',outputFile)

# current year and month
# based on 2018-02-23
#
# This give the list ["2018"],["02"], ["23"]
# This will give a str format for each element
current_date = str.split(time.strftime("%Y %m %d"))
# this is to hold the files that we find that meet the criteria below
files_found = []


# This section will take the current date and determine
# what day of the week was the first day (0 = Monday, 1 = Tuesday, etc...)
# Then it will tell how many days in the given month

def determine_last_day(this_date):
    current_calendar = calendar.monthrange(int(this_date[0]),int(this_date[1]))
    # we just need to return the number of days in this month
    return current_calendar[1]


def remove_old_files():

    # these will both be int to make the math workout
    days_in_month = determine_last_day(current_date)
    current_day_in_month = int(current_date[2])
    message = ""

    for old_logs in old_logfiles:

        stat_info = os.stat(old_logs).st_mtime
            # change the st_mtime info into a datestamp we can use better
        file_time_stamp = str(datetime.datetime.fromtimestamp(stat_info))
        time_split = str.split(file_time_stamp)[0]
            # This just splits the current date so we can parse it out
        file_date = time_split.split("-")
        
        # we only want to do this on the last day of the month!
        if(current_day_in_month == days_in_month):
             # does the file year matches the current year
            if(file_date[0] == current_date[0]):
                    # does the file month match the current month?
                if(file_date[1] == str(current_date[1])):
                    # find the files that the date is less than the current day
                    # make sure both are integers to make the math work!
                    if(int(file_date[2]) < int(current_date[2])):
                        message = "Files found"
                        files_found.append(old_logs)
                    else:
                        message = "No files found"
                else:
                    message = "No files found"
            else:
                message = "No files found"
        else:
            message = "Not the end of the month"

    alog.info(message)

if __name__ == "__main__":
    remove_old_files()






