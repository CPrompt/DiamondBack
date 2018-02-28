#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  read_json.py
#
#  Copyright 2013 Curtis Adkins <curtis@wayne-manor.gotham>
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

import json
import os
import sys
from check_config import check_config
from yaml_log import configure_logger

diamond_back_home = os.path.expanduser(os.path.join('~/.config', 'diamondback'))
diamond_back_config = os.path.join(diamond_back_home, 'diamondback.json')
outputFile = os.path.join(diamond_back_home, 'dback.log')
alog = configure_logger('default',outputFile)

def read_json():
    try:
        json_data = open(diamond_back_config)
        data = json.load(json_data)
    except:
        alog.error("Could not open config file.  Please make sure it exists and is configured")
        # see if we can run the check_config module
        check = check_config()
        check.check_for_configs()
        sys.exit(1)
    return data


def use_list(passed_list):
    return passed_list


def output_config():
    returned_list = read_json()
    config_dict = use_list(returned_list)
    return config_dict

if __name__ == "__main__":
    output_config()

