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
import glob
import logging
from time import strftime
from check_config import check_config
from read_json import output_config

logging.basicConfig(filename='errors.log',level=logging.DEBUG)

myTime = strftime("%Y-%m-%d-%H%M%S")

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
		print "Checking for config files"
		config_check = check_config()
		config_check.check_for_configs()

	#	backup compression
	def compress_backup(self,backupName):

                # check for the config files
                self.check_files()

                # set varialbe names from the read_json file
                backupName = output_config()["backupprefs"]["title"]
                directory_of_backup = output_config()["backupprefs"]["directories"][0]["directoryBackup"]
                redundant_backup_directory = output_config()["backupprefs"]["directories"][0]["redundantBackup"]
                files_for_backup = output_config()["backupprefs"]["files"][0]["filesBackup"]
                ignored_files = output_config()["backupprefs"]["files"][0]["ignoredFiles"]

                # at this point we have confirmed the files needed are there and we can read the config file
                # now we need to make sure the backup directory is actually there and ready

                if(self.directory_is_writable(directory_of_backup)):

                    # start the compression
                    os.system('7z a -t7z -m0=lzma -mx=9 -mfb=64 -ms=on %s_%s.7z -xr!%s -v1024M @%s' % (backupName,myTime,ignored_files,files_for_backup))

                     # Start the backup process
                    file1 = ('%s_%s.7z' % (backupName,myTime))

                     # Create a directory where the backup files will be stored
                    timeDirectory = os.mkdir(directory_of_backup + myTime)
                    tempDir = directory_of_backup + myTime
                    path = os.getcwd()

                     # move the files to the backup directory
                     # need to add the _pylog to this processes
                    for name in glob.glob(path + '//*.7z.*'):
                        shutil.move(name,tempDir)

                else:
                    logging.error("The backup directory does not appear to be set or ready!")
                    sys.exit(1)


                if(self.directory_is_writable(redundant_backup_directory)):
                    os.system('rsync -avz %s %s' % (directory_of_backup,redundant_backup_directory))
                else:
                    logging.error("Either no redundant backup directory exists or it has not been set")
                    sys.exit(1)

