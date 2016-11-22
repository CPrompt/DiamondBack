#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 curtis <curtis@wayne-manor.gotham>
#
# Distributed under terms of the MIT license.

"""
using this to test functions and classes
"""
from check_config import *


def check_files():
    # Check for config directory and files
    print "Checking for config files"
    config_check = check_config()
    config_check.check_for_configs()

check_files()
