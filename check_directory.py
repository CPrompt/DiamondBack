#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  check_directory.py
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
import logging

diamond_back_home = os.path.expanduser(os.path.join('~/.config', 'diamondback'))
diamond_back_config = os.path.join(diamond_back_home, 'diamondback.cfg')
diamond_back_out = os.path.join(diamond_back_home, 'out.log')
diamond_back_filelist = os.path.join(diamond_back_home, 'filelist')

	# list of all the config files and directory
	# we loop through these files one by one to see if they are there
diamond_back_files = (diamond_back_config, diamond_back_out, diamond_back_filelist)

logging.basicConfig(filename='errors.log',level=logging.DEBUG)

class check_directory:

	def directory_is_writable(self,path):
		'''
		Returns True if the specified directory exists and is writable
		by the current user.
		Borrowed from gPodder util.py
		'''
		return os.path.isdir(path) and os.access(path, os.W_OK)

	'''
		This function checks if the files above are there
		If they are not, then it attempts to create the files
		If it has to create the files, then it logs a Warning that
		the program will not function until they are configured
	'''

	def check_for_config_files(self):
		for files in diamond_back_files:
			try:
				with open(files) as f : pass
				print files + " " + "file is there"
				pass
			except IOError as e:
				logging.warning('%s is not there', files)
				#	Try to create file
				files = open(files, 'w+')
				logging.warning("Files had to be created.  Program will not operate correctly until configuration of these files")

	'''
		This function checks if the main configuration directory is readable
		If it is, then it runs the above function to see if the config files are there
		If the directory is not there, it attempts to create the directory and then create the files
		Failing that, it dies with an error log
	'''

	def check_for_configs(self):
		#	first check if the config directory is there
		if (self.directory_is_writable(diamond_back_home)):
			try:
			#	directory is there, move on to files
				newFiles = check_directory()
				newFiles.check_for_config_files()
			except:
				logging.error("Directory is there but could not create files")
		else:
			#	Try to create the config directory
			try:
				os.makedirs(diamond_back_home)
				print "Directory Created"
				#	Now go back and check for config files
				newFiles = check_directory()
				newFiles.check_for_config_files()
			except:
				logging.error("Could not create file")


#	For testing functions
x = check_directory()
x.check_for_configs()
x.check_for_config_files()


