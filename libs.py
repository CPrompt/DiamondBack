#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  libs.py
#
#  Copyright 2012 Curtis Adkins <curtadkins@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import os
import shutil
import sys
import subprocess
import glob
from time import strftime
from check_config import check_config
from read_json import output_config
from config import backupName, directory_of_backup, redundant_backup_directory, files_for_backup, ignored_files, temp_directory, outputFile
from purge_files import remove_old_files
#from log import *
from email_log import email_log_files
from yaml_log import configure_logger

#logger = log_setup()
alog = configure_logger('default',outputFile)

# variables that are used to pass to tar command
myTime = strftime("%Y-%m-%d-%H%M%S")
file_name = backupName + "_" + myTime


class BackupData():


        def directory_is_writable(self,path):
            '''
            Returns True if the specified directory exists and is writable
            by the current user.
            Borrowed from gPodder util.py
            '''
            return os.path.isdir(path) and os.access(path, os.W_OK)

        def check_files(self):
            # Check for config directory and files
            config_check = check_config()
            config_check.check_for_configs()

        # backup compression
        def compress_backup(self,backupName):

            # check for the config files
            self.check_files()

            # at this point we have confirmed the files needed are there and we can read the config file
            # now we need to make sure the backup directory is actually there and ready

            if(self.directory_is_writable(directory_of_backup)):

                # check to see if we need to clear out any previous backups
                remove_old_files()

                # log the start
                #logger.info("Starting the process")
                alog.info("Starting the process")

                # start the compression
                compress_files = subprocess.Popen(["tar","cfv",temp_directory + file_name + ".tar.lzma","--lzma","-T",files_for_backup, "-X",ignored_files],
                        stdout=subprocess.PIPE,stderr=subprocess.PIPE)

                output,err = compress_files.communicate()
                
                rc = compress_files.returncode

                if rc == 0:
                    #logger.info("Backup has completed successfully")
                    alog.info("Backup has completed successfully")
                    email_log_files(output)
                else:
                    #logger.error("There was an error in the backup processes.  Please review the logs further")
                    alog.error("There was an error in the backup processes.  Please review the logs further")
                    #logger.error(rc)
                    alog.error(rc)
                    email_log_files(err)


                # move the files to the backup directory
                for name in glob.glob(temp_directory + '//*.tar.lzma'):
                    shutil.move(name,directory_of_backup)

            else:
                #logger.error("The backup directory does not appear to be set or ready!")
                alog.error("The backup directory does not appear to be set or ready!")
                sys.exit(1)

            if(self.directory_is_writable(redundant_backup_directory)):
                redundant_files = subprocess.Popen(["rsync","-avz",directory_of_backup,redundant_backup_directory],
                        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            else:
                #logger.error("Either no redundant backup directory exists or it has not been set")
                alog.error("Either no redundant backup directory exists or it has not been set")
                sys.exit(1)

