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
#import config
import logging
#import data_log
from data_log import log_action
from time import strftime
#from check_directory import check_directory
from check_config import check_config

logging.basicConfig(filename='errors.log',level=logging.DEBUG)

myTime = strftime("%Y-%m-%d-%H%M%S")

'''
	Need to read the config file so that we can figure out what files
	are being backed up and where they are going
'''


class BackupData():

	def check_files(self):
		# Check for config directory and files
		print "Checking for config files"
		config_check = check_config()
		config_check.check_for_configs()

	#	backup compression
	def compress_backup(self,backupName):

		print directory_of_backup
		#	log the start of the backup
		log_action("start")

		if os.path.exists(directory_of_backup):
			print "Directory is there and ready"

			pass
		else:
			log_action("error")
			raise OSError ("Directory does not exist!")

		# need to output this data to the log file as well
		os.system('7z a -t7z -m0=lzma -mx=9 -mfb=64 -ms=on %s_%s.7z -xr!%s -v1024M @%s' % (backupName,myTime,ignored_files,files_for_backup))


		#	Start the backup process
		file1 = ('%s_%s.7z' % (backupName,myTime))

		#	Create a directory where the backup files will be stored
		timeDirectory = os.mkdir(directory_of_backup + myTime)
		tempDir = directory_of_backup + myTime
		path = os.getcwd()

		#	move the files to the backup directory
		# 	need to add the _pylog to this processes
		for name in glob.glob(path + '//*.7z.*' & path + '//*_pylog'):
			shutil.move(name,tempDir)

		#	log the end of the process and completion
		log_action("end")
		log_action("complete")


		#  Need something here that will determine if we want to do a redundant backup
		#  Possible just looking to see if the redundant_backup section is complete
		#  in the config file.  If it is, then we need to make sure the path
		#  specified is reachable

		'''
		redundantTime = strftime("%Y-%m-%d-%H%M%S")
		redundantAction = " ***** Starting RSync Process ***** \n"
		redundantAction = redundantAction + "%s \n" % (redundantTime)
		self.logAction(redundantTime)
		'''

		'''
		os.system('rsync -avz %s %s' % (directory_of_backup,redundant_directory))
		redundantEnd = strftime("%Y-%m-%d-%H%M%S")
		redundantEndAction = "Rsync Complete at %s \n" % (redundantEnd)
		redundantEndAction = redundantEndAction + "*******************************************************************"
		self.logAction(redundantEndAction)
		'''
		#	Look at the config file for the redundant backup directory
		#	and make sure it exists
		if directory_is_writable(redundant_backup_directory):
			print "Redundant directory is there and ready"
		else:
			print "Redundant directory is not there"
			logging.error("Redundant directory is not there")

