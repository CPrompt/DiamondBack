#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  check_config.py
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
import json

diamond_back_home = os.path.expanduser(os.path.join('~/.config', 'diamondback'))
diamond_back_config = os.path.join(diamond_back_home, 'diamondback.json')
diamond_back_filelist = os.path.join(diamond_back_home, 'filelist')

# list of all the config files and directory
# we loop through these files one by one to see if they are there
diamond_back_files = (diamond_back_config, diamond_back_filelist)

data = {
    "backupprefs": {

        "title": "BACKUP",

        "directories": [{
            "directoryBackup": "/path/to/main/backup/",
            "redundantBackup": "/path/to/redundant/backup/"
        }],

        "files": [{
            "filesBackup": "/home/user/.config/diamondback/filelist",
            "outputFile": "/home/user/.config/diamondback/out.log",
            "ignoredFiles": "/home/user/.config/diamondback/ignored"
        }]

    }
}

logging.basicConfig(filename='error.log',level=logging.DEBUG)

class check_config:

    def directory_is_writable(self,path):
        return os.path.isdir(path) and os.access(path, os.W_OK)


    def check_for_config_files(self):
        for files in diamond_back_files:
            try:
                with open(files) as f : pass
                pass
            except IOError as e:
            # Try to create file
                for files in diamond_back_files:
                    if(files == diamond_back_config):
                        with open(diamond_back_config, 'w') as outfile:
                            json.dump(data, outfile, sort_keys = True, indent = 4)
                            outfile.close()
                            logging.warning("Config file had to be created.  Program will not operate correctly until configuration of these files")
                    else:
                        files = open(files, 'w+')
                        logging.warning("%s had to be created.  Program will not operate correctly until configuration of these files" % (files))


    def check_for_configs(self):
        # first check if the config directory is there
        if (self.directory_is_writable(diamond_back_home)):
            try:
                self.check_for_config_files()
            except:
                print("ERROR! Had issues checking for config files and directories!")
                logging.error("Directory is there but could not create files")
        else:
            try:
                os.makedirs(diamond_back_home)
                print("Directory Created")
                # Now go back and check for config files
                self.check_for_config_files()
            except:
                logging.error("Could not create file")
                # if the config directory isn't there, we can go no further
                # end the program
                sys.exit(1)


