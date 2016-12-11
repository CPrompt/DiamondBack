#!/usr/bin/python

import os
import time
import glob
import datetime
from datetime import date
import calendar
from read_json import output_config
from config import backupName, directory_of_backup, redundant_backup_directory, files_for_backup, ignored_files

log_directory = directory_of_backup
old_logfiles = glob.glob(os.path.join(log_directory, '*.*'))


# current year and month
current_date = str.split(time.strftime("%Y %m"))
current_weekday = str.split(time.strftime("%d"))

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


    # REMOVE THIS FROM HERE....
    #days_in_month = days_in_month - 8
    #print(days_in_month)
    # TO HERE

    for old_logs in old_logfiles:
        stat_info = os.stat(old_logs).st_mtime
        # change the st_mtime infor into a datestamp we can use better
        file_time_stamp = str(datetime.datetime.fromtimestamp(stat_info))
        time_split = str.split(file_time_stamp)[0]

        # This just splits the current date so we can parse it out
        dic_date = time_split.split("-")

        # we only want this to process on the last day of the month
        if(current_day_in_month == days_in_month):
            # if the month of the file is the same as the current month
            if(int(dic_date[1]) == int(current_date[1])):
                # if the day of the log file is less than the last day of the month
                #if(int(dic_date[2]) < int(determine_last_day(current_date))):
                if(int(dic_date[2]) < int(days_in_month)):
                    # here we are going to try to delete records.
                    #print(old_logs)
                    try:
                        os.remove(old_logs)
                    except:
                        print("Could not remove files")
                else:
                    print("No files to remove")
        else:
            print("Still more days until the end of the month")








