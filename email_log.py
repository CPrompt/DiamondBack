#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  email_log.py
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
# Email to localhost.  This will take the place of cron sending the email when moved to systemd service

import smtplib
from config import email_for_logs, email_server

email_log_subject = "DiamondBack Logs"

def email_log_files(log_text):
    log_text = bytes.decode(log_text)
    msg = "Subject: %s\n%s" %(email_log_subject,log_text)
    s = smtplib.SMTP(email_server)
    s.sendmail(email_for_logs,email_for_logs,msg)
    s.quit()


