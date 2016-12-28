#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 curtis <curtis@wayne-manor.gotham>
#
# Distributed under terms of the MIT license.

"""
import the variables from the json file
read by the read_json.py module
"""


from read_json import output_config


# set varialbe names from the read_json file
backupName = output_config()["backupprefs"]["title"]
directory_of_backup = output_config()["backupprefs"]["directories"][0]["directoryBackup"]
redundant_backup_directory = output_config()["backupprefs"]["directories"][0]["redundantBackup"]
files_for_backup = output_config()["backupprefs"]["files"][0]["filesBackup"]
ignored_files = output_config()["backupprefs"]["files"][0]["ignoredFiles"]
email_for_logs = output_config()["backupprefs"]["email_for_logs"]
email_server = output_config()["backupprefs"]["email_server"]


#diamond_back_home = os.path.expanduser(os.path.join('~/.config', 'diamondback'))
#diamond_back_config = os.path.join(diamond_back_home, 'diamondback.json')
#diamond_back_filelist = os.path.join(diamond_back_home, 'filelist')
