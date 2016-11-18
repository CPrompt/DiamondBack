#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  data_log.py
#
#  Copyright 2012 Curtis Adkins <curtis@wayne-manor>
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

'''
	#	This file is used to output the data of each attempt to backup
	#	Other instances will be in the "errors.log" file
'''

import sys
from check_config import *

from time import strftime

def capture_time():
	current_time = strftime("%Y-%m-%d-%H%M%S")
	return current_time

#	error logging
def log_action(my_action):
	try:
		check_for_configs()

		saveout = sys.stdout
		fsock = open(diamond_back_out, 'a')
		sys.stdout = fsock

		#	capture the current time
		capture_time()

		my_log = "******************************************************************* \n"

		if my_action == "start":
			capture_time()
			my_log = my_log +  "Backup Starting at : %s  \n" % (capture_time())
			print my_log
		elif my_action == "end":
			capture_time()
			my_log = "Backup Complete at : %s  \n" % (capture_time())
			print my_log
		elif my_action == "complete":
			capture_time()
			my_log = "BACKUP_%s has been compressed and moved \n" % (capture_time())  + my_log
			print my_log
		elif my_action == "error":
			capture_time()
			my_log = "ERROR! Directory does not exist!"
			print my_log
		else:
			print my_action

		sys.stdout = saveout
		fsock.close()
	except:
		print "ERROR!"

'''

	Usage

log_action("start")
log_action("complete")
log_action("end")
log_action("Type whatever you want here")

'''

#log_action("test")
