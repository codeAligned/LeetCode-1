#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from crontab import CronTab

#init cron
cron   = CronTab()

#add new cron job
job  = cron.new(command='network.py', comment='testing')

#job settings
job.minute.on(15)
